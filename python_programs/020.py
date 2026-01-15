def isWoodball(num):
    if num<=0:
        return False
    n=1
    while True:
        woodball = n*(2**n)-1

        if woodball==num:
            return True
        if woodball>num:
            return False
        n+=1

print(isWoodball(0)) #No
print(isWoodball(-234))  #No
print(isWoodball(383)) #yes
print(isWoodball(200)) #No
