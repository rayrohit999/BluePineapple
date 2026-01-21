'''
Broadcasting Practice
 -Create a (4, 5) matrix of random floats.
 -Create a (5,) vector and add it to every row using broadcasting.
 -Normalize each row to sum to 1 (handle division carefully).
'''

import numpy as np

arr = np.random.rand(4, 5)
print("Created Array: \n", arr)

#creating vector (5, )
vector = np.random.rand(5)
print("\n Vecotr: \n", vector)

#Adding vector to every row
brod_arr = arr + vector
print("\n Broadcasted Array:\n", brod_arr)

#normalize each row so that it sums to 1
row_sum = np.sum(arr, axis=1, keepdims=True)
normalized_arr = arr/row_sum
print("\nRow-normalized Array:\n", normalized_arr)

print("\nRow sums after normalization:\n", np.sum(normalized_arr, axis=1))

