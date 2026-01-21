'''
Add Derived Columns
 -Using quantity, unit_price, discount_pct:
    compute gross_amount = quantity * unit_price
    compute net_amount = gross_amount * (1 - discount_pct/100)
 -Add a is_high_value flag (net_amount > threshold).
'''
import numpy as np
import pandas as pd

#reading csv file
df = pd.read_csv("./orders.csv")
print("first five row of data frame: \n", df.head())

# calculating gross_amount
df["gross_amount"] = df["quantity"] * df["unit_price"]
print("\nFirst five rows with new column(gross_amount): \n", df.head())

# calculating net_amount
df["net_amount"] = df["gross_amount"] * (1 - df["discount_pct"] / 100)
print("\nFirst five rows with new column(net_amount): \n", df.head())

# adding flag column is_high_value true if net amount is greater than 10000
df["is_high_value"] = df["net_amount"] > 10000 
print("\nFirst five rows with new column(is_high_value): \n", df.head())

#exporting this updated dataframe to orders_updated.csv to use it in next assignments
df.to_csv("orders_updated.csv", index=False)