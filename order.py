import random
from datetime import datetime, timedelta

NUM_ORDERS = 500_000
MAX_USERS = 100_000  # adjust based on your Users table

def random_date():
    """Generate a random date within the last 2 years."""
    start_date = datetime.now() - timedelta(days=730)
    random_days = random.randint(0, 730)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

with open("orders.sql", "w", encoding="utf-8") as f:
    for order_id in range(1, NUM_ORDERS + 1):
        user_id = random.randint(1, MAX_USERS)
        order_date = random_date()

        f.write(
            f"INSERT INTO Orders (OrderID, UserID, OrderDate) "
            f"VALUES ({order_id}, {user_id}, '{order_date}');\n"
        )

print("✅ 500,000 Orders generated in orders.sql")