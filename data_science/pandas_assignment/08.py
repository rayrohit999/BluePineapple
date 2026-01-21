'''
Window Functions (Intermediate)
 -For each customer:
    sort by order_date
    compute prev_order_date
    compute days_since_prev
    compute rolling 3-order average net_amount
 -Identify customers whose average order value is increasing (simple heuristic).
''' 

import numpy as np
import pandas as pd

# loading dataset
customer_df = pd.read_csv("./customers.csv")
orders_df = pd.read_csv("./orders_updated.csv")
customer_df["signup_date"] = pd.to_datetime(customer_df["signup_date"])
orders_df["order_date"] = pd.to_datetime(orders_df["order_date"])
#merging both dataframes to perform calculations
merged_df = pd.merge(customer_df, orders_df, on="customer_id")

#sorting by customer and order date
merged_df = merged_df.sort_values(by = ["customer_id", "order_date"])


# Window functions
# Previous order date per customer
merged_df["previous_order_date"] = merged_df.groupby("customer_id")["order_date"].shift(1)

# days since previous order
merged_df["days_since_prev"] = (merged_df["order_date"] - merged_df["previous_order_date"]).dt.days


# rolling 3 days average of net amount
merged_df["rolling_3d_avg_net_amount"] = (
    merged_df
    .groupby("customer_id")["net_amount"]
    .rolling(window=3, min_periods=1)
    .mean()
    .reset_index(level=0, drop=True)
)
print(merged_df)

# Heuristic : increasing average order value
# compare last rolling avg vs first rolling avg

customer_trend = (
    merged_df
    .groupby("customer_id")
    .agg(
        first_avg = ("rolling_3d_avg_net_amount", "first"),
        last_avg = ("rolling_3d_avg_net_amount", "last")
    )
)

customer_trend["average_order_value_increasing"] = customer_trend["last_avg"] > customer_trend["first_avg"]


# customer with increasing average order value
increasing_customers = customer_trend[customer_trend["average_order_value_increasing"]].reset_index()
# print(customer_trend)
print("Increasing customer\n", increasing_customers)