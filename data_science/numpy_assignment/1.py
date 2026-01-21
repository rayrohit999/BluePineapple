import numpy as np
arr = np.arange(1, 21)
print("Created Array: \n", arr)
print("Shape: ", np.shape(arr))
print("dype: ", arr.dtype)
print("Min: ", np.min(arr))
print("Max: ", np.max(arr))
print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))


arr.dtype = "float64"
print("Updated dtype: ", arr.dtype)