# personalized_real_estate_agent

## Project Setup

The projects uses pipenv for creating the virtual environment and installing the required dependencies. Just run the following command:
    
    pipenv install
    pipenv shell

For running the project, just run:

    python project.py

## Generated Listings

The project automatically generate real state listings using a LLM (Google's Gemini). They are store in a lanceDB database in the directory homematch_db. they are also store in a CVS file called listings.csv. 

The project doesn't create the listings if the lanceDB already exists. If you want to generate them again, just remove the homematch_db directory.

## Execution

There is a file "buyers_preferences.py" that contains a list of preferences for different buyers. Once the project is executed, personal listings are created based on those preferences and shown at the end of the execution with the following format:

    * Buyer preferences
    * House that best matches the buyer preferences
    * Personal listing for the given house and buyer preferences.

The following is an example of the output:

    Buyer 0 preferences:

    **Buyer Preferences:**

    * **Size:** 2 bedrooms, 1 bathroom
    * **Amenities:**
        * Serene Hills neighborhood
        * Modern kitchen
        * Living room with natural light
        * Backyard with mature trees
        * Large living room and bedrooms with good light
    * **Transportation:** Proximity to a major highway
    * **Neighborhood:** Urban
    
    Recommended house:

    {'Neighborhood': 'Serene Hills', 'Price': 350000, 'Bedrooms': 2, 'Bathrooms': 1, 'House Size': 1200, 'Description': 'Nestled in the tranquil Serene Hills neighborhood, this cozy 2-bedroom, 1-bathroom home offers a peaceful retreat. Step inside to discover a bright and airy living room with large windows overlooking the lush backyard. The updated kitchen features granite countertops, stainless steel appliances, and ample cabinet space. Both bedrooms are generously sized and offer plenty of natural light. The backyard is a private oasis with a covered patio, mature trees, and a fire pit, perfect for relaxing and entertaining. Enjoy the serenity of Serene Hills in this charming and affordable home.', 'Neighborhood Description': 'Serene Hills is a family-friendly neighborhood known for its rolling hills, tree-lined streets, and community spirit. Residents enjoy access to a community pool, playground, and hiking trails. The neighborhood is conveniently located near schools, shopping, and public transportation.', '_distance': 0.2727991044521332}
    
    Personalize listing:

    **Dear Prospective Buyer,**

    I am delighted to present to you this exceptional property in the highly sought-after Serene Hills neighborhood. With its charming curb appeal and meticulously maintained interior, this home is the perfect fit for your lifestyle and preferences.

    **Unmatched Amenities and Comfort:**

    * This cozy 2-bedroom, 1-bathroom home offers a perfect balance of space and functionality.
    * Step inside to discover a bright and airy living room with large windows, inviting ample natural light.
    * The modern kitchen boasts granite countertops, stainless steel appliances, and generous cabinet space, making cooking a delight.
    * Both bedrooms are generously sized and feature plenty of natural light, creating a serene and inviting atmosphere.
    * The backyard is a private sanctuary with a covered patio, mature trees, and a fire pit, providing the perfect setting for relaxation and entertainment.

    **Neighborhood Charm and Convenience:**

    * Serene Hills is a family-friendly neighborhood renowned for its rolling hills, tree-lined streets, and strong community spirit.
    * Residents enjoy access to a community pool, playground, and hiking trails, offering endless opportunities for recreation and leisure.
    * The neighborhood's convenient location near schools, shopping, and public transportation ensures effortless access to essential amenities.

    **Proximity to Major Highway:**

    * While Serene Hills offers a tranquil retreat, it is also conveniently located near a major highway. This provides easy access to the city center and surrounding areas, making your daily commute a breeze.

    **Urban Living in a Tranquil Setting:**

    * Serene Hills strikes the perfect balance between urban convenience and suburban tranquility.
    * While you can enjoy the amenities of city life, you can also retreat to the peace and quiet of your own private oasis.

    **Exceptional Value:**

    * At $350,000, this home represents an exceptional value in the highly desirable Serene Hills neighborhood.
    * Its combination of amenities, location, and charm makes it an investment that will appreciate over time.

    I am confident that this property will exceed your expectations and provide you with the perfect home you have been searching for. I would be honored to schedule a private showing at your earliest convenience.

    Sincerely,
    [Your Name]
    Real Estate Agent

    ++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++

    Buyer 1 preferences:

    **Buyer Preferences:**

    * **Property:**
        * Comfortable three-bedroom house with a spacious kitchen and cozy living room
    * **Amenities:**
        * Quiet neighborhood
        * Fitness centers and hiking trails
    * **Transportation:**
        * Easy access to a reliable bus line
        * Proximity to a major highway
        * Bike-friendly roads
    * **Other:**
        * Large principal bedroom
        * Nice backyard
        * Modern kitchen
    
    Recommended house:

    {'Neighborhood': 'Cozy Creek', 'Price': 450000, 'Bedrooms': 3, 'Bathrooms': 2, 'House Size': 1800, 'Description': 'Step into the warmth and charm of this 3-bedroom, 2-bathroom home nestled in the heart of Cozy Creek. The inviting living room features a cozy fireplace and large windows overlooking the private backyard. The updated kitchen boasts granite countertops, stainless steel appliances, and a breakfast nook. The spacious master suite offers a walk-in closet and a private bathroom with a soaking tub. Enjoy outdoor living on the covered patio or gather around the fire pit in the fenced-in backyard. This charming home is perfect for families and those seeking a sense of community.', 'Neighborhood Description': 'Cozy Creek is a friendly and welcoming neighborhood with a strong sense of community. Residents enjoy access to a community pool, playground, and walking trails. The neighborhood is conveniently located near schools, shopping, and public transportation.', '_distance': 0.424929678440094}
    
    Personalize listing:

    **Dear Prospective Homeowner,**

    I am delighted to present to you this exceptional property at 450000 in the highly sought-after Cozy Creek neighborhood. This meticulously maintained 3-bedroom, 2-bathroom home perfectly aligns with your preferences and offers an array of desirable features that will elevate your lifestyle.

    **Property Highlights:**

    * **Spacious and Inviting:** Step into the warmth and charm of this home, featuring a generous living room adorned with a cozy fireplace and large windows that flood the space with natural light.
    * **Gourmet Kitchen:** Unleash your culinary creativity in the updated kitchen, boasting granite countertops, stainless steel appliances, and a breakfast nook that provides ample space for casual dining.
    * **Private Master Suite:** Retreat to the spacious master suite, complete with a walk-in closet and a private bathroom featuring a soaking tub, creating a sanctuary for relaxation and rejuvenation.
    * **Outdoor Oasis:** Extend your living space to the covered patio and fenced-in backyard, perfect for hosting gatherings, enjoying outdoor meals, or simply basking in the sunshine.

    **Neighborhood Amenities:**

    * **Cozy Creek Community:** Embrace the vibrant spirit of Cozy Creek, where residents enjoy access to a community pool, playground, and walking trails, fostering a sense of belonging and camaraderie.
    * **Fitness and Recreation:** Stay active and healthy with the nearby fitness centers and hiking trails, offering ample opportunities for physical pursuits and connecting with nature.

    **Transportation Convenience:**

    * **Bus Line Accessibility:** Commute with ease thanks to the reliable bus line located nearby, providing convenient access to various destinations.
    * **Highway Proximity:** Enjoy seamless travel with the major highway just a short distance away, connecting you to major cities and destinations.
    * **Bike-Friendly Roads:** Explore the neighborhood and surrounding areas on two wheels, as the bike-friendly roads provide a safe and enjoyable cycling experience.

    **Additional Features:**

    * **Large Principal Bedroom:** The master bedroom provides ample space for a king-sized bed, ensuring a comfortable and luxurious sleeping experience.
    * **Nice Backyard:** The fenced-in backyard offers privacy and ample space for gardening, entertaining, or simply relaxing in the fresh air.
    * **Modern Kitchen:** The kitchen's sleek and modern design, complete with high-end appliances and granite countertops, will inspire culinary adventures and impress your guests.

    I am confident that this home will exceed your expectations and provide you with the perfect balance of comfort, convenience, and lifestyle amenities. I highly recommend scheduling a private tour to fully appreciate the exceptional qualities of this property.

    Sincerely,
    Your Real Estate Agent

    ++++++++++++++++++++++++++++++++++++++
    ++++++++++++++++++++++++++++++++++++++

    Buyer 2 preferences:

    **Buyer Preferences:**

    * **Size:** 4-5 bedrooms, 4 bathrooms
    * **Must-Haves:**
        * Ample space for entertaining
        * Proximity to water bodies for nautical activities
        * Convenience to shopping
    * **Amenities:**
        * Heated pool
        * Spacious living areas
        * High-end kitchen
    * **Transportation:**
        * Easy access to highways
    * **Neighborhood:**
        * Urban or suburban setting with good shopping options
    
    Recommended house:

    {'Neighborhood': 'Tranquil Shores', 'Price': 2000000, 'Bedrooms': 4, 'Bathrooms': 3, 'House Size': 3000, 'Description': "Welcome to your waterfront paradise in the exclusive Tranquil Shores neighborhood. This stunning 4-bedroom, 3-bathroom home offers breathtaking views of the sparkling lake from every room. The grand foyer leads to a spacious living room with soaring ceilings and a wall of windows overlooking the water. The gourmet kitchen is a chef's dream with a large center island, top-of-the-line appliances, and a butler's pantry. The master suite is a luxurious retreat with a private balcony, a spa-like bathroom, and a walk-in closet. Step outside to the backyard oasis featuring a heated pool, outdoor kitchen, and a private dock. Live the ultimate waterfront lifestyle in this exceptional Tranquil Shores home.", 'Neighborhood Description': 'Tranquil Shores is a prestigious gated community offering an unparalleled waterfront lifestyle. Residents enjoy access to a private marina, a community clubhouse, and 24-hour security. The neighborhood is conveniently located near upscale shopping, fine dining, and top-rated schools.', '_distance': 0.3349783420562744}
    
    Personalize listing:

    **Dear [Buyer's Name],**

    I'm delighted to introduce you to an exceptional waterfront property in the prestigious Tranquil Shores neighborhood that perfectly aligns with your preferences.

    **Tranquil Shores Home Highlights:**

    * **Spacious and Entertaining:** This stunning 4-bedroom, 3-bathroom home boasts 3,000 square feet of living space, providing ample room for entertaining and family gatherings.

    * **Waterfront Paradise:** Nestled on the shores of a sparkling lake, this home offers breathtaking views from every room. Step outside to the backyard oasis, complete with a heated pool and private dock, where you can enjoy nautical activities and the serenity of waterfront living.

    * **Convenient Location:** Tranquil Shores is conveniently located near upscale shopping and dining options, fulfilling your desire for proximity to amenities. The neighborhood also offers easy access to highways for effortless commuting.

    **Neighborhood Features:**

    * **Urban-Suburban Blend:** Tranquil Shores seamlessly combines the conveniences of urban living with the tranquility of a suburban setting. It features a gated community with 24-hour security, ensuring privacy and peace of mind.

    * **Shopping Haven:** The neighborhood is surrounded by an array of shopping options, from boutiques to grocery stores, catering to your everyday needs and desires.

    * **Community Amenities:** Residents enjoy access to a private marina, a community clubhouse, and a variety of recreational facilities, fostering a sense of community and active lifestyle.

    **Additional Perks:**

    * **Heated Pool:** Indulge in year-round swimming and relaxation in the comfort of your own backyard.

    * **Spacious Living Areas:** The grand foyer leads to a spacious living room with soaring ceilings and a wall of windows, creating an inviting and airy ambiance.

    * **High-End Kitchen:** The gourmet kitchen is equipped with top-of-the-line appliances, a large center island, and a butler's pantry, making it a culinary haven.

    This exceptional Tranquil Shores home offers an unparalleled blend of waterfront living, convenience, and luxury. It seamlessly fulfills your preferences and will provide you with a lifestyle of comfort, relaxation, and adventure.

    I highly recommend scheduling a private tour to experience the beauty and amenities of this remarkable property firsthand. Please don't hesitate to contact me if you have any questions or would like to arrange a viewing.

    Sincerely,
    [Your Name]
    Real Estate Agent