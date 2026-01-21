'''
GroupBy Aggregations
Group by city and compute:
    total orders
    unique customers
    total revenue (sum net_amount)
    average order value
Sort by revenue desc and show top 10 cities.
'''
import numpy as np
import pandas as pd
# loading dataset
df = pd.read_csv("./orders_updated.csv")


# # creating group by city
# city_group_df = df.groupby("city")

# #calculating total orders per city
# total_orders = city_group_df.agg(total_order = ("customer_id", "count"))
# print("Total orders per city: \n", total_orders)

# # counting unique customers per city
# unique_customers = city_group_df["customer_id"].nunique()
# print("Unique custormer per city: \n", unique_customers)

# # calculating total revenue per city
# total_revenue = city_group_df["net_amount"].sum()
# print("Total revenue per city: \n", total_revenue)

# # calculating average order value per city
# average_order_value = city_group_df["net_amount"].mean()
# print("Average order value: \n", average_order_value)

city_summary = (
    df.groupby("city")
      .agg(
          total_orders=("order_id", "count"),
          unique_customers=("customer_id", "nunique"),
          total_revenue=("net_amount", "sum"),
          average_order_value=("net_amount", "mean")
      )
      .sort_values(by="total_revenue", ascending=False)
      .head(10)
)

# Output
print(city_summary)
