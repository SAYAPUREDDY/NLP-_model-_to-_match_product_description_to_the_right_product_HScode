# As we cant get the real data now we gonna use some synthetic data for our modeling purpose
#import the necessary libraries
import random
import pandas as pd

# Updated Categories for generating product descriptions
categories = [
    "Wireless mouse",
    "Bluetooth speaker",
    "Gaming keyboard",
    "Fitness tracker",
    "Electric kettle",
    "Smartwatch",
    "Digital camera",
    "Portable charger",
    "Noise-cancelling headphones",
    "Smart thermostat",
    "Wi-Fi router",
    "Electric toothbrush",
    "Coffee maker",
    "Air fryer",
    "Microwave oven",
    "Smart TV",
    "Robot vacuum cleaner",
    "3D printer",
    "VR headset",
    "Electric scooter",
    "Portable air conditioner",
    "Smart door lock",
    "Dash camera",
    "Portable blender",
    "Water purifier",
    "Gaming console",
    "Smart light switch",
    "Electric standing desk",
    "Office chair",
    "Smartphone holder",
    "Home security camera",
    "Wireless charging pad",
    "Smart refrigerator",
    "Smart washing machine",
    "Bluetooth tracker",
    "Noise-cancelling earbuds",
    "Smart LED strip",
    "Portable projector",
    "Electric heater",
    "Smart air purifier",
    "Smart baby monitor",
    "Wireless presentation remote",
    "Digital picture frame",
    "Portable tire inflator",
    "Bluetooth car kit",
    "Home theater system",
    "Smart scale",
    "Smart mirror",
    "Smart water bottle",
    "Portable solar charger"
]

# Updated adjectives and attributes to make the descriptions
colors = ["black", "white", "silver", "red", "blue", "green", "yellow", "gold", "pink", "purple"]
sizes = ["compact", "small", "medium", "large", "extra-large", "portable"]
materials = ["plastic", "metal", "aluminum", "steel", "ceramic", "glass", "carbon fiber"]
additional_attributes = ["wireless", "water-resistant", "rechargeable", "energy-efficient", "Bluetooth-enabled", "smart", "portable", "touchscreen", "voice-controlled", "app-connected"]

# Function to generate a random and unique HS code
def generate_unique_hs_code(existing_codes):
    while True:
        hs_code = f"{random.randint(1000, 9999)}.{random.randint(10, 99)}"
        if hs_code not in existing_codes:
            existing_codes.add(hs_code)
            return hs_code

data = []
used_hs_codes = set()  
#loop to get the different product description
for i in range(5000):
    product_type = random.choice(categories)
    color = random.choice(colors)
    size = random.choice(sizes)
    material = random.choice(materials)
    attribute = random.choice(additional_attributes)
    
    # Creating the product description
    description = f"{size} {material} {product_type.lower()}, {color}, {attribute}"
    # this particular line is responsible for generating the unique hscodes
    hs_code = generate_unique_hs_code(used_hs_codes)
    data.append([description, hs_code])

df = pd.DataFrame(data, columns=["Product Description", "HS Code"])

df.to_csv("product_description_hscode_data.csv", index=False)

print(df.head())
