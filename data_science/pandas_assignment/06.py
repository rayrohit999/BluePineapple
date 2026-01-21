'''
Handling Missing Values
 -Randomly introduce missing values in city, payment_mode, and discount_pct.
 -Apply different strategies:
    fill categorical with “Unknown”
    fill numeric with median by category
 -Prove it worked: show missing counts before/after.
'''
import numpy as np
import pandas as pd

df = pd.read_csv("./orders_updated.csv")

# introducing missing value randomly
np.random.seed(42)
missing_frac = 0.2  # 20% missing
for col in ["city", "payment_mode", "discount_pct"]:
    df.loc[df.sample(frac=missing_frac).index, col] = np.nan

# Missing value before cleaning
print("Missing values BEFORE cleaning:")
print(df[["city", "payment_mode", "discount_pct"]].isna().sum())
print("\n")

# 1. Filling categorical with unknown
category_col = ["city", "payment_mode"]
df[category_col] = df[category_col].fillna("unknown")

# 2. Filling numeric with median by category
df["discount_pct"] = df.groupby("category")["discount_pct"].transform(lambda x: x.fillna(x.median()))

# Missing value after cleaning
print("Missing values BEFORE cleaning:")
print(df[["city", "payment_mode", "discount_pct"]].isna().sum())
