def sortList(list):
    digitList=[i for i in list if str(i).isdigit()]
    strList=[i for i in list if not str(i).isdigit()]
    digitList.sort()
    strList.sort()
    return digitList+strList

print(sortList([1,2,3,4,"a","A",'B','b',"rohit",123]))
print(sortList([1,2,3,4,"a","A",'B','b',"rohit",4,123]))
print(sortList([]))
print(sortList([1,2,3,4,123]))
print(sortList(["a","A",'B','b',"rohit"]))
print(sortList([1,2,3,4,"a","A",'B','b',"rohit","rahul","rohit",123]))