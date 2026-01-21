'''
Fancy Indexing + Scatter Update
 -Create a length-30 zero array.
 -Randomly pick 8 unique positions and set them to 1.
 -Then set positions divisible by 5 to 9 (overwriting if needed).
'''

import numpy as np
zeroes_arr = np.zeros(30, dtype="int64")
print("Arrys created of Zeros: \n", zeroes_arr)

#Randomly pick 8 unique positions and set them to 1
zeroes_arr[np.random.choice(zeroes_arr.size, size=8, replace=False)] = 1
print("\nAfter assigning 1 to random 8 positions: \n", zeroes_arr)


#Then set positions divisible by 5 to 9 (overwriting if needed).
pos = np.concatenate(([0], np.arange(4, zeroes_arr.size, 5)))
print(pos)
zeroes_arr[pos] = 9
print("\nAfter seting position divisible by 5 to 9:\n", zeroes_arr)