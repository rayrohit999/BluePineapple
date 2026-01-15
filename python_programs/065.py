# def sum_recursion(arr):
#     length = len(arr)
#     if length == 0 :
#         return 0
#     return arr[length -1] + sum_recursion(arr[:length - 1])

def sum_recursion(arr,i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_recursion(arr,i+1)
if __name__ == "__main__":
    print(sum_recursion([1,2,3,4,5]))

