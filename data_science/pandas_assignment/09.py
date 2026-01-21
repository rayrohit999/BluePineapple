'''
Outlier Detection + Capping (Intermediate)
 -For each category:
    compute IQR of net_amount
    flag outliers (outside [Q1-1.5IQR, Q3+1.5IQR])
    cap outliers to bounds (winsorize)
 -Report outlier counts by category before/after.
'''

import numpy as np
import pandas as pd
#importing data
df = pd.read_csv("./orders_updated.csv")

#Finding IQR
IQR_each_category = (
    df
    .groupby("category")["net_amount"]
    .agg(
        Q1=lambda x: x.quantile(0.25),
        Q3=lambda x: x.quantile(0.75),
        IQR=lambda x: x.quantile(0.75) - x.quantile(0.25)
    )
)

IQR_each_category["lower"] = IQR_each_category["Q1"] - 1.5 * IQR_each_category["IQR"]
IQR_each_category["upper"] = IQR_each_category["Q3"] + 1.5 * IQR_each_category["IQR"]

df = df.merge(IQR_each_category, on="category")

# flag outliers before
df["is_outlier_before"] = (
    (df["net_amount"] < df["lower"]) |
    (df["net_amount"] > df["upper"])
)

# winsorize (cap)
df["net_amount_capped"] = df["net_amount"].clip(
    lower=df["lower"],
    upper=df["upper"]
)

# flag outliers after
df["is_outlier_after"] = (
    (df["net_amount_capped"] < df["lower"]) |
    (df["net_amount_capped"] > df["upper"])
)

# report
outlier_report = (
    df
    .groupby("category")
    .agg(
        outliers_before=("is_outlier_before", "sum"),
        outliers_after=("is_outlier_after", "sum")
    )
)

print(outlier_report)
