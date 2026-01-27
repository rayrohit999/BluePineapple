def get_first_or_specified(arr,row = None,column = None):
    if not row and not column:
        result = []
        for list in arr:
            result.append(list[0])
        return result
    else:
        try:
            return arr[row][column]
        except Exception as e:
            return e
    

if __name__ == "__main__":
    nums = [
        [1,2,3,4],
        [2,3,4,5],
        [6,7,8,9],
        [12,33,43,12]
    ]

    ans = get_first_or_specified(nums) #[1,2,6,12]
    print(ans)
    ans = get_first_or_specified(nums,3,4) #error
    print(ans)
    ans = get_first_or_specified(nums,3,2) #43
    print(ans)