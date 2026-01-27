'''
Write a function to find the triplet with sum of the given array
'''
def calculate_all_triplet_sum(input_array: list[int]) -> list[int]:
    '''
    Takes list of integers as input and calculate sum of all the triplets and returns them as a list
        Parameter: 
            input_array(list): list of integers
        Returns:
            list of sum of triplets
    '''
    if len(input_array) < 3:
        raise Exception("Function expect atl east 3 elements in input list")
    result = []
    arrLength = len(input_array)
    for i in range(arrLength):
        for j in range(i + 1, arrLength):
            for k in range(j + 1, arrLength):
                result.append((input_array[i] + input_array[j] + input_array[k]))
    return result

if __name__ == "__main__":
    try:
        input_array = [1,2,3,4]
        sum_array = calculate_all_triplet_sum(input_array)
        print(sum_array)

        input_array = []
        sum_array = calculate_all_triplet_sum(input_array)
        print(sum_array)
    except Exception as e:
        print(e)