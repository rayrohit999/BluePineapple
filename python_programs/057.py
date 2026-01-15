def generateLargest(digits):
    #sort the list in decending order
    digits.sort(reverse = True)
    #form the number
    largestNum = 0
    for digit in digits:
        largestNum = largestNum *10 +digit
    return largestNum
print(generateLargest([1,2,3,0,9,4,5,3]))
print(generateLargest([]))