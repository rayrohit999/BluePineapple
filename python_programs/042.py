import collections
def sumOfRepeted(arr):
    count = collections.Counter(arr)
    sum = 0
    for key, value in count.items():
        if value>1:
            sum = sum + (key*value)
    return sum

print(sumOfRepeted([1,1,1,2,2,2,33,3])) #Output: 9
print(sumOfRepeted([])) #Output: 0
print(sumOfRepeted([1,2,3,4,5,6,7])) #Output: 0
