import random

NUM_ORDER_ITEMS = 1_000_000
NUM_ORDERS = 500_000     # Existing orders
NUM_PRODUCTS = 100_000   # Existing products

with open("data_orderitems.sql", "w", encoding="utf-8") as f:
    for i in range(1, NUM_ORDER_ITEMS + 1):
        order_id = random.randint(1, NUM_ORDERS)
        product_id = random.randint(1, NUM_PRODUCTS)
        quantity = random.randint(1, 5)

        f.write(
            f"INSERT INTO OrderItems (ItemID, OrderID, ProductID, Quantity) "
            f"VALUES ({i}, {order_id}, {product_id}, {quantity});\n"
        )

        # Optional: progress update every 100k
        if i % 100_000 == 0:
            print(f"{i} order items generated...")

print("✅ 1,000,000 OrderItems generated in data_orderitems.sql!")