'''
Pivot Table Dashboard View
 -Create a pivot:
    index: month (from order_date )
    columns: category
    values: net_amount sum
 -Add a “Grand Total” column and compute month-over-month growth %.
'''
import numpy as np
import pandas as pd

# Loading dataset
df = pd.read_csv("./orders_updated.csv")

# Ensuring datetime & extracting month
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M").astype(str)

# Creating pivot table
pivot_df = pd.pivot_table(
    df,
    index="month",
    columns="category",
    values="net_amount",
    aggfunc="sum",
    fill_value=0
)


# Adding Grand Total column
pivot_df["Grand_Total"] = pivot_df.sum(axis=1)


# Month-over-Month Growth %
pivot_df["MoM_Growth_%"] = pivot_df["Grand_Total"].pct_change() * 100

# output
print(pivot_df)
