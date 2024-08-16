import pandas as pd
import random

# Define product classes and attributes
product_classes = {
    'car': {
        'colors': ['red', 'blue', 'black', 'white'],
        'sizes': ['compact', 'sedan', 'SUV', 'truck'],
        'models': ['2023', '2024', '2025'],
        'hs_code': '870320'
    },
    'bike': {
        'colors': ['red', 'black', 'green', 'blue'],
        'sizes': ['small', 'medium', 'large'],
        'models': ['mountain', 'road', 'hybrid'],
        'hs_code': '871190'
    },
    'watch': {
        'colors': ['black', 'silver', 'gold', 'blue'],
        'sizes': ['small', 'medium', 'large'],
        'batteries': ['AA', 'AAA', 'rechargeable'],
        'hs_code': '910211'
    },
    'clothes': {
        'colors': ['red', 'blue', 'green', 'black'],
        'sizes': ['S', 'M', 'L', 'XL'],
        'fabrics': ['cotton', 'wool', 'polyester'],
        'hs_code': '620293'
    },
    'mobile': {
        'colors': ['black', 'white', 'blue', 'red'],
        'sizes': ['5.5 inch', '6 inch', '6.5 inch'],
        'batteries': ['3000mAh', '4000mAh', '5000mAh'],
        'compatibilities': ['4G', '5G'],
        'hs_code': '851712'
    }
}

# Function to generate descriptions based on product class
def generate_description(product_class):
    attributes = product_classes[product_class]
    color = random.choice(attributes.get('colors', ['']))
    size = random.choice(attributes.get('sizes', ['']))
    model = random.choice(attributes.get('models', ['']))
    battery = random.choice(attributes.get('batteries', ['']))
    fabric = random.choice(attributes.get('fabrics', ['']))
    compatibility = random.choice(attributes.get('compatibilities', ['']))
    
    if product_class == 'car':
        return f"{color} {product_class} model {model}, size {size}"
    elif product_class == 'bike':
        return f"{color} {product_class}, size {size}, model {model}"
    elif product_class == 'watch':
        return f"{color} {product_class}, size {size}, battery {battery}"
    elif product_class == 'clothes':
        return f"{color} {product_class}, size {size}, fabric {fabric}"
    elif product_class == 'mobile':
        return f"{color} {product_class}, size {size}, battery {battery}, compatibility {compatibility}"
    return ""

# Generate 3,000 samples
num_samples = 3000
data = {
    'description': [],
    'hs_code': []
}

for i in range(num_samples):
    # Randomly select a product class
    product_class = random.choice(list(product_classes.keys()))
    description = generate_description(product_class)
    hs_code = product_classes[product_class]['hs_code']
    
    # Add to data dictionary
    data['description'].append(description)
    data['hs_code'].append(hs_code)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('product_hs_code_data.csv', index=False)

print("Sample dataset with 3,000 entries has been created and saved to 'product_hs_code_data.csv'.")

