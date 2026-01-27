def missing_ranges(nums: list[int], start: int, end: int) -> list[str]:
    temp = []
    result = []
    for i in range(start, end + 1):
        if not i in nums:
            temp.append(i)
        else :
            if temp:
                minRange = min(temp)
                maxRange = max(temp)
                if minRange != maxRange:
                    result.append(str(minRange) + "-" + str(maxRange))
                    temp.clear()
                if minRange == maxRange:
                    result.append(str(minRange))
                    temp.clear()
    if temp:
        minRange = min(temp)
        maxRange = max(temp)
        if minRange != maxRange:
            result.append(str(minRange) + "-" + str(maxRange))
            temp.clear()
        if minRange == maxRange:
            result.append(str(minRange))
            temp.clear()
    return result

if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75,98]
    start = 0
    end = 99
    print(missing_ranges(nums, start, end)) # ["2", "4-49", "51-74", "76-99"]