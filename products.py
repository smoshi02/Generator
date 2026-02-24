import random

NUM_PRODUCTS = 100_000
NUM_CATEGORIES = 1000  # your categories table

adjectives = [
    "Premium", "Ultra", "Smart", "Eco", "Pro", "Advanced",
    "Portable", "Compact", "Wireless", "Gaming", "Classic",
    "Modern", "Heavy Duty", "Lightweight", "Deluxe", "Mini", "Max", "Plus"
]

# Expanded product types for variety
product_types = [
    "Laptop", "Headphones", "Smartphone", "Backpack", "Desk", "Chair", "Watch", "Camera",
    "Shoes", "T-Shirt", "Blender", "Microwave", "Keyboard", "Mouse", "Basketball", "Dumbbell",
    "Guitar", "Printer", "Tablet", "Monitor", "Power Bank", "Router", "Coffee Maker", "Air Fryer",
    "Fan", "Jacket", "Sofa", "Bed Frame", "Helmet", "Speaker", "Water Bottle", "Sunglasses",
    "Desk Lamp", "Bookshelf", "Notebook", "Pen Set", "Smartwatch", "Vacuum Cleaner", "Drone",
    "Tripod", "Gaming Chair", "Yoga Mat", "Treadmill", "Electric Scooter", "Hair Dryer",
    "Perfume", "Lipstick", "Blender Bottle", "Camera Lens", "Projector", "Camping Tent",
    "Sleeping Bag", "Hiking Boots", "Smart Thermostat", "Smart Light Bulb", "Air Conditioner",
    "Rice Cooker", "Juicer", "Tablet Stand", "Phone Case", "Wireless Charger", "Bluetooth Speaker",
    "Electric Kettle", "Suitcase", "Backpack Cooler", "Car Seat Cover", "Pet Bed", "Dog Leash",
    "Cat Toy", "Board Game", "Puzzle", "Painting Set", "Craft Kit", "Bike Helmet", "Skateboard",
    "Scooter", "Fishing Rod", "Tent Lamp", "Binoculars", "Laptop Stand", "Monitor Arm", "Keyboard Tray",
    "Mouse Pad", "Desk Organizer", "Water Filter", "Air Purifier", "Smart Door Lock", "Security Camera",
    "Smart Plug", "Digital Frame", "Coffee Grinder", "Espresso Machine", "Blender Pro", "Meat Grinder",
    "Ice Cream Maker", "Popcorn Machine", "Bread Maker", "Smart Scale", "Electric Toothbrush",
    "Massage Gun", "Treadmill Pro", "Exercise Bike", "Rowing Machine", "Elliptical Trainer",
    "Jump Rope", "Fitness Tracker", "Resistance Bands", "Foam Roller", "Medicine Ball"
]

with open("data_products.sql", "w", encoding="utf-8") as f:
    used_names = set()

    for i in range(1, NUM_PRODUCTS + 1):
        category_id = random.randint(1, NUM_CATEGORIES)

        # Ensure unique product name
        while True:
            name = f"{random.choice(adjectives)} {random.choice(product_types)}"
            if name not in used_names:
                used_names.add(name)
                break

        price = round(random.uniform(50, 5000), 2)

        f.write(
            f"INSERT INTO Products (ProductID, CategoryID, ProductName, Price) "
            f"VALUES ({i}, {category_id}, '{name}', {price});\n"
        )

print("✅ 100,000 unique products generated in data_products.sql!")