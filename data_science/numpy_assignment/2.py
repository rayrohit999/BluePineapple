import numpy as np
arr = np.random.randint(1, 100, size = 50)
print("Created array: \n", arr)

evenNumbers = arr[arr % 2 == 0]
print("\nEven Numbers: ",evenNumbers)

numbers_divisible_by_theree_and_greater_than_fifty = arr[(arr % 3 == 0) & (arr > 50)]
print("\nNumbers divisible by 3 and greater than 50 : \n", numbers_divisible_by_theree_and_greater_than_fifty)

arr[arr < 20] = 20
print("\nArray after filled numbers less than 20 with 20: \n", arr)