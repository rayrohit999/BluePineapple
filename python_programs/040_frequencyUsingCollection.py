from collections import Counter
def getFrequency(lists):
    
    freq = Counter()
    for sublist in lists:
        freq.update(sublist)
    return freq


nums=[
        [1,2,6],
        [1,3,4,5,7,8],
        [1,3,5,6,8,9],
        [2,5,7,11],
        [1,4,7,8,12]
    ]
print(getFrequency(nums))   