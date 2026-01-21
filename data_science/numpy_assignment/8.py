'''
Missing Values Simulation
 -Create a 1D float array of size 40.
 -Randomly turn 20% positions into np.nan.
 -Compute mean ignoring NaNs.
 -Replace NaNs with the median of non-NaN values.
'''
import numpy as np

#creating arry with random value between 5 and 50
arr = np.random.randint(5, 50, size=40).astype(float)
print("Created Array: \n", arr)

# filling 20% position with np.nan
num_nan = int(0.2 * arr.size)
nan_indices = np.random.choice(arr.size, num_nan, replace=False)
arr[nan_indices] = np.nan
print("\nArray with NaNs:\n", arr)

# Computing mean ignoring NaNs
mean_value = np.nanmean(arr)
print("\nMean (ignoring NaNs):", mean_value)

# Computing median ignoring NaNs
median_value = np.nanmedian(arr)

# Replace NaNs with median
arr[np.isnan(arr)] = median_value

print("\nArray after replacing NaNs with median:\n", arr)