def countPositive(list):
    count = 0
    for value in list:
        if value > 0:
            count += 1
    return count

print(countPositive([2,3,4,5,-25,-4,-3,-1,2])) 
print(countPositive([])) 
