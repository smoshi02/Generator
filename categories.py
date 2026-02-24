import random

NUM_CATEGORIES = 1000

categories = [
    "Electronics", "Mobile Phones", "Laptops", "Tablets", "Cameras",
    "Clothing - Men", "Clothing - Women", "Clothing - Kids",
    "Shoes", "Accessories",
    "Home & Kitchen", "Furniture", "Appliances",
    "Sports Equipment", "Fitness", "Outdoor Gear",
    "Books", "Educational Materials", "Office Supplies",
    "Toys", "Baby Products",
    "Beauty & Cosmetics", "Health & Wellness",
    "Automotive", "Motorcycle Parts",
    "Pet Supplies", "Gaming", "Music Instruments",
    "Groceries", "Snacks", "Beverages",
    "Jewelry", "Watches",
    "Garden Supplies", "Hardware Tools",
    "Art Supplies", "Craft Materials",
    "Travel Accessories", "Luggage",
    "Smart Home Devices", "Computer Accessories"
]

with open("data_categories.sql", "w", encoding="utf-8") as f:
    for i in range(1, NUM_CATEGORIES + 1):
        category_name = random.choice(categories)

        f.write(
            f"INSERT INTO Categories (CategoryID, CategoryName) "
            f"VALUES ({i}, '{category_name}');\n"
        )

print("✅ 1000 Category INSERT statements generated!")