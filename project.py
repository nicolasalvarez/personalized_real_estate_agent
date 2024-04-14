import json
import os

import google.generativeai as genai
import lancedb
import pandas as pd
import pyarrow as pa

from buyers_preferences import answers, questions

# DB Config
DB_URI = "homematch_db"
R_S_L_TABLE_NAME = "real_state_listings"
NO_REAL_STATE_LISTINGS = 10

# Gemini Pro configuration parameters.
TEMP = 0.7
TOP_P = 0.8
TOP_K = 40
MAX_OUTPUT_TOKENS = 4096

# Just default values for safety settings at the moment.
SAFETY_SETTINGS = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

def get_gemini_model():
    # Set up the model.
    generation_config = {
        "temperature": TEMP,
        "top_p": TOP_P,
        "top_k": TOP_K,
        "max_output_tokens": MAX_OUTPUT_TOKENS,
    }

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                    generation_config=generation_config,
                                    safety_settings=SAFETY_SETTINGS)
    return model


def initialize_db():
    db = lancedb.connect(DB_URI)
    schema = pa.schema([pa.field("vector", pa.list_(pa.float32(), list_size=768)),
                        pa.field("Neighborhood", pa.string()),
                        pa.field("Price", pa.uint32()),
                        pa.field("Bedrooms", pa.uint8()),
                        pa.field("Bathrooms", pa.uint8()),
                        pa.field("House Size", pa.uint16()),
                        pa.field("Description", pa.string()),
                        pa.field("Neighborhood Description", pa.string())]
                        )

    try:
        db.create_table(R_S_L_TABLE_NAME, schema=schema)
    except Exception:
        print(f"Table {R_S_L_TABLE_NAME} already exists")
    return db


def generate_real_state_listings(model, no_real_state_listings):
    prompt = """
Generate a realistic real estate listing with the following information: Neighborhood, Price (between 100000 and 5000000), Bedrooms (between 1 and 5), Bathrooms (between 1 and 4), House Size (between 1000 and 10000), Description, and Neighborhood Description.

Return the output as:
{
"Neighborhood": "Green Oaks",
"Price": 800000,
"Bedrooms": 3,
"Bathrooms": 2,
"House Size": 2000,
"Description": "Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.",
"Neighborhood Description": "Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze."
}
"""
    real_state_listings = []
    messages = [{"role": "user", "parts": prompt}]
    for i in range(no_real_state_listings):
      response = model.generate_content(messages)
      messages.append(response.candidates[0].content)
      messages.append({'role':'user', 'parts': ['Generate another one different but different from the previous ones.']})
      real_state_listing = json.loads(response.text)
      embedding = genai.embed_content(model="models/embedding-001",
                                      content=response.text,
                                      task_type="SEMANTIC_SIMILARITY")
      real_state_listing["vector"] = embedding["embedding"]

      real_state_listings.append(real_state_listing)
      pd.DataFrame(real_state_listings).drop('vector', axis=1).to_csv("listings.csv")

    return real_state_listings


def get_buyer_preference(model, question, answer):
    q_and_a = "".join(f"f{question}: {answer}\n" for question, answer in zip(question, answer))
    prompt = f"Generate a summary of the buyer preferences given the following questions and answers:\n{q_and_a}"
    response = model.generate_content(prompt)
    embedding = genai.embed_content(model="models/embedding-001",
                                      content=response.text,
                                      task_type="SEMANTIC_SIMILARITY")["embedding"]

    return {"vector": embedding, "buyer_preference": response.text}


def get_personalize_listing(model, buyer_preference, recommended_houses):
    recommended_houses.pop("vector")
    prompt = f"""You are a real state agent and you want to sell a house with the following specs:\n {recommended_houses.to_string()}
    
    Given a buyer with the following preferences: {buyer_preference}, try to convince him to buy the house.
    """
    response = model.generate_content(prompt)

    return response.text


def main():
    # Initialize the DB
    db = initialize_db()
    r_s_l_table = db.open_table(R_S_L_TABLE_NAME)

    model = get_gemini_model()

    # Generate data only in the r_s_l_table is empty
    if len(r_s_l_table.to_pandas()) == 0:
        real_state_listings = generate_real_state_listings(model, NO_REAL_STATE_LISTINGS)
        r_s_l_table.add(real_state_listings)

    for buyer in range(len(answers)):
        # Get the buyer preferences
        buyer_preference = get_buyer_preference(model, questions, answers[buyer])

        # Find the most suitable house given the buyer preferences
        recommended_house = r_s_l_table.search(buyer_preference["vector"]).limit(1).to_pandas()

        # Get a personalize listing for the gien house.
        personalize_listing = get_personalize_listing(model, buyer_preference["buyer_preference"], recommended_house)
        
        print(f"++++++++++++++++++++++++++++++++++++++\n"
              f"++++++++++++++++++++++++++++++++++++++\n\n"
              f"Buyer {buyer} preferences:\n\n{buyer_preference['buyer_preference']}\n"
              f"Recommended house:\n\n{recommended_house.to_dict(orient="records")[0]}\n"
              f"Personalize listing:\n\n{personalize_listing}\n"
              )

if __name__ == "__main__":
    main()