'''
Joins / Merges (Customers + Orders)
 -Create a customers DataFrame: customer_id, signup_date, segment.
 -Merge with orders.
 -Compute revenue by segment and retention proxy:
        “active in last 60 days” per segment.
'''
import numpy as np
import pandas as pd

#creating dataframe
customers_df = pd.read_csv("./customers.csv")
orders_df = pd.read_csv("./orders_updated.csv")

# merging customers dataframe to orders dataframe
merged_df = pd.merge(customers_df, orders_df, on="customer_id")
merged_df["order_date"]=pd.to_datetime(merged_df["order_date"])
print(merged_df)
# revenue by segment
revenue_by_segment = (
    merged_df
    .groupby("segment", as_index=False)["net_amount"]
    .sum()
    .rename(columns={"net_amount": "total_revenue"})
)
print("Totoal revenue by segment:")
print(revenue_by_segment)

#retension proxy
latest_order_date = merged_df["order_date"].max()
cutoff_date = latest_order_date - pd.Timedelta(days = 60)

# customer active in last 60 days per segment
active_customers = (merged_df[merged_df["order_date"] >= cutoff_date]
                    .groupby("segment", as_index=False)["customer_id"]
                    .nunique()
                    # .reset_index(name="active_customers_60d")
                    .rename(columns={"customer_id":"active_customers_60d"})
                )

print(active_customers)