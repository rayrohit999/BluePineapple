# def countSubstring(str):
#     count =0
#     length = len(str)
#     for i in range(length):
#         for j in range(i,length):    O(n*n)
#             if str[i]==str[j]:
#                 count +=1
#     return count

from collections import Counter
def countSubstring(str):
    freq = Counter(str)
    total=0
    for value in freq.values():
        total += (value * (value+1))//2   # no of substring can be formed is k*(k+1)//2 where k is count of character
    return total


print(countSubstring("")) #0
print(countSubstring("a")) #1
print(countSubstring("abc")) #3
print(countSubstring("bbb")) #6
print(countSubstring("abcab")) #7
print(countSubstring("abab")) #6
print(countSubstring("AaA")) #4
print(countSubstring("1123")) #5