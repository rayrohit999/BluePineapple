'''
Cohort Analysis (Intermediate)
 -Define cohort month = customer’s first order month.
 -For each cohort, compute:
    number of active customers by month offset (M0, M1, M2…)
    retention rate matrix (cohort table)
 -Output as a DataFrame shaped like a retention heatmap table (values as %).
'''
import pandas as pd

#loading dataset
df = pd.read_csv("./orders.csv")
df["order_date"] = pd.to_datetime(df["order_date"])

#create order month
df["order_month"] = df["order_date"].dt.to_period("M")


#defining cohort month(first order month per customer)
df["cohort_month"] = (
    df
    .groupby("customer_id")["order_month"]
    .transform("min")
)


# computing month offset m0, m1...
df["cohort_index"] = (
    (df["order_month"].dt.year - df["cohort_month"].dt.year) * 12 +
    (df["order_month"].dt.month - df["cohort_month"].dt.month)
)
print(df)

# count active customers per cohort per month
cohort_count = (
    df
    .groupby(["cohort_month", "cohort_index"])["customer_id"]
    .nunique()
    .reset_index()
    .rename(columns = {"customer_id" : "Number of active customer"})
)
print("\n Cohort count: ")
print(cohort_count)

cohort_table = cohort_count.pivot(
    index = "cohort_month",
    columns = "cohort_index",
    values = "Number of active customer"
)
print("\n Cohort Table:")
print(cohort_table)

# convert count to retension percentage
cohort_size = cohort_table[0]

retension = cohort_table.divide(cohort_size, axis = 0) * 100
retension = retension.round(2)

retension.columns = [f"M{int(col)}" for col in retension.columns]
print("\nRetension Table: ")
print(retension)
