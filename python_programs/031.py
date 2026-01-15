#make a heap of size k and mangae to do push pop

def kTopElements(nums,k):
    from collections import defaultdict
    
    d=defaultdict(int)
    for row in nums:
        for i in row:
            d[i]+=1

    print(d)
    temp=[]
    import heapq
    for key,v in d.items():
        if len(temp)<k:
            temp.append((v,key))
            if len(temp)==k:
                heapq.heapify(temp)
        else:
            if temp[0][0]<v:
                heapq.heappop(temp)
                heapq.heappush(temp,(v,key))
        
    result=[]
    while temp:
        v,key = heapq.heappop(temp)
        result.append(key)
    return result
if __name__=="__main__":
    nums=[
        [1,2,6],
        [1,3,4,5,7,8],
        [1,3,5,6,8,9],
        [2,5,7,11],
        [1,4,7,8,12]
    ]
    print(kTopElements(nums,3))