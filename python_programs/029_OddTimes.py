from collections import Counter

def oddTimes(arr):
    result=[]
    count=Counter(arr)
    for item,value in count.items():
        if value%2 !=0 :
            result.append(item)
    return result



#implementation
lst = [1, 2, 3, 2, 3, 1, 3]
print(oddTimes(lst)) #[3]

lst = []
print(oddTimes(lst)) #[]

lst = [1, 2, 3, 2, 3, 1]
print(oddTimes(lst)) #[]

lst = [1, 2, 3, 2, 3, 1,1,3]
print(oddTimes(lst)) #[1,3]