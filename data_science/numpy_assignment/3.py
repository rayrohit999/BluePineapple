'''
3. Reshape + Axis Operations
 -Create an array from 1 to 60 and reshape into (5, 12).
 -Compute:
    row-wise sums
    column-wise means
    global std
 -Find the index of the maximum value in the 2D array
'''
import numpy as np
arr = np.arange(1, 61)
arr.shape = (5, 12)
print("Crated Array: \n", arr)

#row-wise sums
rowSum = np.sum(arr, axis = 1)
print("\nRow wise sum: \n", rowSum)

#column-wise means
colwise_mean = np.mean(arr, axis = 0)
print("\n Column wise mean: \n", colwise_mean)

#global std
std = np.std(arr)
print("\n Global Standard Deviation: \n", std)

#index of maximum value in 2D array
row, col = np.where(arr == np.max(arr))
print("\nIndex of maximum value in 2D array: ", "Row: ", row, "Col: ", col)