import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/orders_returns.csv')

# Basic info
print("Data Shape:", df.shape)
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'])

# 🔸 Overall return rate
overall_return_rate = df['return_status'].mean() * 100
print(f"Overall Return Rate: {overall_return_rate:.2f}%")

# 🔹 Return rate by category
category_returns = df.groupby('category')['return_status'].mean().sort_values(ascending=False) * 100
print("\nReturn Rate by Category:")
print(category_returns)

# 🔹 Return rate by supplier
supplier_returns = df.groupby('supplier')['return_status'].mean().sort_values(ascending=False) * 100
print("\nReturn Rate by Supplier:")
print(supplier_returns)

# 🔹 Return rate by marketing channel
channel_returns = df.groupby('marketing_channel')['return_status'].mean().sort_values(ascending=False) * 100
print("\nReturn Rate by Channel:")
print(channel_returns)

# 🔹 Return rate by location
location_returns = df.groupby('customer_location')['return_status'].mean().sort_values(ascending=False) * 100
print("\nReturn Rate by Location:")
print(location_returns)

# 🔹 Plots
plt.figure(figsize=(10,6))
sns.barplot(x=category_returns.index, y=category_returns.values)
plt.title('Return Rate by Product Category')
plt.ylabel('Return Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
