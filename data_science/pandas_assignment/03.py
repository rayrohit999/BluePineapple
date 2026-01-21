'''
Filtering + Multi-condition Queries
 -Filter orders:
    category in a set (e.g., Electronics/Fashion)
    net_amount > X
    order_date within last N days (relative to max date)
 -Output count + total net_amount.
'''
import numpy as np
import pandas as pd

# Loading updated data from assignment 2
df = pd.read_csv("./orders_updated.csv")

# chaning datatype to ensure correct calculation
df["order_date"] = pd.to_datetime(df["order_date"])

#Filtering Orders
category = ("Electronics", "Fashion")
X = 10000
N = 60

max_date = df["order_date"].max()
cutoff_date = max_date - pd.Timedelta(days=N)

filtered_df = df[
    (df["category"].isin(category)) &
    (df["net_amount"] > X) &
    (df["order_date"] >= cutoff_date)
]

#output:
print("Max order date:", max_date)
print("Cutoff date:", cutoff_date)
print("\nFiltered Orders:")
print(filtered_df)

print("\nSummary:")
print("Order count:", filtered_df.shape[0])
print("Total net amount:", filtered_df["net_amount"].sum())