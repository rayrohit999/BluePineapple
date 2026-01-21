'''
Create + Inspect + Basic Cleaning
 -Create a DataFrame from a dict (at least 10 rows).
 -Show .head(), .info(), .describe(include="all").
 -Convert a date column to datetime.
 -Trim whitespace from string columns.
'''

import numpy as np
import pandas as pd

#hardcoded sample data
dict_data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "customer": [
        " Alice ", "Bob", " Charlie", "David ", " Eve ",
        "Frank", " Grace ", "Heidi", " Ivan ", "Judy "
    ],
    "order_date": [
        "2024-01-01", "2024-01-03", "2024-01-05", "2024-01-07",
        "2024-01-10", "2024-01-12", "2024-01-15", "2024-01-18",
        "2024-01-20", "2024-01-22"
    ],
    "sales": [250, 300, 150, 400, 500, 350, 275, 450, 325, 600]
}

#creating dataframe
df = pd.DataFrame(dict_data)

# .head() will print first 5 rows from dataframe
print("df.head()\n", df.head()) 

# .info()
print("\ndf.info()\n")
df.info()

# .describe(include="all")
print("\ndf.describe()\n", df.describe(include="all"))

# Converting date column to datetime
df['order_date'] = pd.to_datetime(df['order_date'])
#Checking datatype of order_date column using df.info()
print("\nUpdated INFO: \n")
df.info()
# Trim whitespace from string columns.
string_cols = df.select_dtypes(include="object").columns
df[string_cols] = df[string_cols].apply(lambda x: x.str.strip())