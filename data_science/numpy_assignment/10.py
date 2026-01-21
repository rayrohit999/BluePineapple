'''
Time Series Rolling Window Stats
 -Create a 1D array representing 365 days of random “daily sales”.
 -Compute rolling 7-day mean and rolling 30-day mean using NumPy (no pandas).
 -Detect days where sales are > (rolling_30_mean + 2*rolling_30_std).
'''

import numpy as np

np.random.seed(27)

daily_sales = np.random.randint(50, 200, size=365)
print("Crated dataset: \n", daily_sales)

#Rolling windows
rollingWindow7 = np.lib.stride_tricks.sliding_window_view(daily_sales, 7)
rollingWindow30 = np.lib.stride_tricks.sliding_window_view(daily_sales, 30)


rolling7Mean = rollingWindow7.mean(axis = 1)
rolling30Mean = rollingWindow30.mean(axis = 1)
rolling30Std = rollingWindow30.std(axis = 1)

print("\nRolling 7 days mean:\n", rolling7Mean)
print("\nRolling 30 days mean: \n", rolling30Mean)
# Align sizes (rolling stats start later)
sales_aligned = daily_sales[29:]  # first 29 days have no 30-day window

# Anomaly detection
anomaly_threshold = rolling30Mean + 2 * rolling30Std
anomaly_days = np.where(sales_aligned > anomaly_threshold)[0] + 29

# Output
print("\nTotal days:", len(daily_sales))
print("Number of anomalies detected:", len(anomaly_days))
print("Anomalous day indices:", anomaly_days)
