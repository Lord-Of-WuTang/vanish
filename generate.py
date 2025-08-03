import random
import csv
from datetime import datetime, timedelta

# Simulate 500 customer transactions over 6 months
def generate_transaction():
    name = f"Customer{random.randint(1, 500)}"
    date = datetime.now() - timedelta(days=random.randint(0, 180))
    amount = round(random.uniform(1000, 50000), 2)
    device = random.choice(['mobile', 'desktop'])
    category = random.choice(['electronics', 'fashion', 'home', 'beauty'])
    return [name, date.strftime('%Y-%m-%d'), amount, device, category]

# Save to CSV
with open('vanishing_customers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer Name', 'Date', 'Amount', 'Device', 'Category'])
    for _ in range(500):
        writer.writerow(generate_transaction())

print("✅ Data story CSV 'vanishing_customers.csv' created.")
