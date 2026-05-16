import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker()
np.random.seed(42)

# Configuration
NUM_RECORDS = 5000
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 5, 16)

# Generate date range
date_range = pd.date_range(start=START_DATE, end=END_DATE, freq='H')
dates = np.random.choice(date_range, size=NUM_RECORDS, replace=True)

# Generate data
data = {
    'Order_ID': [f'ORD{str(i).zfill(6)}' for i in range(1, NUM_RECORDS + 1)],
    'Customer_ID': [f'CUST{str(random.randint(1, 1000)).zfill(4)}' for _ in range(NUM_RECORDS)],
    'Customer_Name': [fake.name() for _ in range(NUM_RECORDS)],
    'Customer_Email': [fake.email() for _ in range(NUM_RECORDS)],
    'Order_Date': sorted(dates),
    'Product_Category': np.random.choice(
        ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books'],
        size=NUM_RECORDS
    ),
    'Product_Name': np.random.choice(
        ['Laptop', 'Smartphone', 'T-Shirt', 'Jeans', 'Desk Lamp', 'Yoga Mat', 
         'Running Shoes', 'Novel', 'Monitor', 'Keyboard', 'Mouse', 'Headphones'],
        size=NUM_RECORDS
    ),
    'Quantity': np.random.randint(1, 5, NUM_RECORDS),
    'Unit_Price': np.random.uniform(10, 1000, NUM_RECORDS).round(2),
    'Discount_Percent': np.random.choice([0, 5, 10, 15, 20], NUM_RECORDS),
    'Customer_Segment': np.random.choice(['Premium', 'Standard', 'Budget'], NUM_RECORDS),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], NUM_RECORDS),
    'Payment_Method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'UPI'], NUM_RECORDS),
    'Delivery_Days': np.random.randint(1, 15, NUM_RECORDS),
    'Customer_Satisfaction': np.random.randint(1, 6, NUM_RECORDS),
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate derived columns
df['Total_Price'] = (df['Unit_Price'] * df['Quantity']).round(2)
df['Discount_Amount'] = (df['Total_Price'] * df['Discount_Percent'] / 100).round(2)
df['Final_Amount'] = (df['Total_Price'] - df['Discount_Amount']).round(2)
df['Profit_Margin'] = (df['Final_Amount'] * 0.25).round(2)  # 25% margin assumption
df['Order_Month'] = df['Order_Date'].dt.to_period('M')
df['Order_Year'] = df['Order_Date'].dt.year
df['Return_Status'] = np.random.choice(['No Return', 'Returned', 'Partial Return'], 
                                       NUM_RECORDS, p=[0.85, 0.10, 0.05])

# Export to CSV
df.to_csv('ecommerce_sales_data.csv', index=False)
print(f"✅ Dataset generated successfully!")
print(f"📊 Total records: {len(df)}")
print(f"📁 File saved as: ecommerce_sales_data.csv")
print(f"\nDataset Preview:")
print(df.head(10))
print(f"\nDataset Info:")
print(df.info())