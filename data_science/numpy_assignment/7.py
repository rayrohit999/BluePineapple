'''
Sorting + Top-K Without Full Sort
 -Create 100 random numbers (floats).
 -Find top 10 values and their indices using an efficient approach (argpartition).
 -Print top 10 sorted descending (values + indices aligned).
'''
import numpy as np
arr = np.random.rand(100)
print("Created Array: \n", arr)

top10_idx = np.argpartition(arr, -10)[-10:]
print("Top 10 indexes are: ", top10_idx)

top10_vals = arr[top10_idx]
print("Top 10 values: ", top10_vals)

# Sort top 10 in descending order 
sorted_order = np.argsort(top10_vals)[::-1]
top10_idx_sorted = top10_idx[sorted_order] 
top10_vals_sorted = top10_vals[sorted_order] 
# Print results 
print("\nTop 10 values (descending) with indices:") 
for idx, val in zip(top10_idx_sorted, top10_vals_sorted): 
    print(f"Index: {idx}, Value: {val}")