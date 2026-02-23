import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

random.seed(42)
np.random.seed(42)

# Configuration
N = 10000
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

regions = {
    "North America": ["USA", "Canada", "Mexico"],
    "Europe": ["Germany", "France", "UK", "Italy", "Spain"],
    "Asia Pacific": ["China", "Japan", "Australia", "India"],
    "Latin America": ["Brazil", "Argentina", "Colombia"]
}

products = {
    "Electronics": ["Laptops", "Smartphones", "Tablets", "Accessories"],
    "Furniture": ["Chairs", "Desks", "Shelves", "Sofas"],
    "Office Supplies": ["Paper", "Pens", "Notebooks", "Printers"],
    "Clothing": ["Shirts", "Pants", "Shoes", "Jackets"]
}

segments = ["Consumer", "Corporate", "Home Office"]

# Price ranges per category
price_ranges = {
    "Electronics": (200, 2000),
    "Furniture": (100, 1500),
    "Office Supplies": (10, 300),
    "Clothing": (20, 500)
}

rows = []
for i in range(N):
    # Random date
    delta = end_date - start_date
    rand_days = random.randint(0, delta.days)
    order_date = start_date + timedelta(days=rand_days)

    # Region and country
    region = random.choice(list(regions.keys()))
    country = random.choice(regions[region])

    # Product
    category = random.choice(list(products.keys()))
    subcategory = random.choice(products[category])

    # Pricing
    unit_price = round(random.uniform(*price_ranges[category]), 2)
    quantity = random.randint(1, 10)
    revenue = round(unit_price * quantity, 2)
    cost = round(revenue * random.uniform(0.5, 0.8), 2)
    profit = round(revenue - cost, 2)
    profit_margin = round((profit / revenue) * 100, 2)

    # Customer
    segment = random.choice(segments)

    rows.append({
        "order_id": f"ORD-{i+1:05d}",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "year": order_date.year,
        "quarter": f"Q{(order_date.month - 1) // 3 + 1}",
        "month": order_date.month,
        "month_name": order_date.strftime("%B"),
        "region": region,
        "country": country,
        "category": category,
        "subcategory": subcategory,
        "customer_segment": segment,
        "quantity": quantity,
        "unit_price": unit_price,
        "revenue": revenue,
        "cost": cost,
        "profit": profit,
        "profit_margin": profit_margin
    })

df = pd.DataFrame(rows)
df = df.sort_values("order_date").reset_index(drop=True)
df.to_csv("data/global_retail_sales.csv", index=False)

print(f"✅ Dataset u krijua me sukses!")
print(f"📊 Totali i transaksioneve: {len(df)}")
print(f"📅 Periudha: {df['order_date'].min()} deri {df['order_date'].max()}")
print(f"💰 Revenue total: ${df['revenue'].sum():,.2f}")
print(f"\nKolumnat: {list(df.columns)}")
