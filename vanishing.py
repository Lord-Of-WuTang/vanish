import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('vanishing_customers.csv', parse_dates=['Date'])

# Basic overview
print("📊 Data Overview:")
print(df.info())
print(df.describe())

# 🗓️ Purchases Over Time
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Amount'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='teal')
plt.title('Monthly Purchase Trend')
plt.ylabel('Total Sales Amount')
plt.xlabel('Month')
plt.grid(True)
plt.tight_layout()
plt.show()

# 📱 Device Comparison
device_sales = df.groupby('Device')['Amount'].sum()

plt.figure(figsize=(6, 4))
device_sales.plot(kind='bar', color=['orange', 'blue'])
plt.title('Sales by Device Type')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 🛍️ Product Category Performance
category_sales = df.groupby('Category')['Amount'].sum().sort_values()

plt.figure(figsize=(8, 5))
category_sales.plot(kind='barh', color='purple')
plt.title('Sales by Product Category')
plt.xlabel('Total Sales')
plt.tight_layout()
plt.show()

# 🔍 Bounce Rate Simulation (Optional)
# Simulate bounce rates for mobile vs desktop
import numpy as np
df['BounceRate'] = df['Device'].apply(lambda x: np.random.uniform(0.4, 0.7) if x == 'mobile' else np.random.uniform(0.1, 0.3))
bounce_avg = df.groupby('Device')['BounceRate'].mean()

plt.figure(figsize=(6, 4))
bounce_avg.plot(kind='bar', color=['red', 'green'])
plt.title('Average Bounce Rate by Device')
plt.ylabel('Bounce Rate')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
