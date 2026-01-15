from functools import reduce
def findCommon(input_list: list[list[int]]) -> list[int]:
    '''
    Takes list of list as input and returns the common element in all the lists
        Parameter:
            input_list(list[list[int]]): Contains list of lists which have integers
        Returns:
            result(list): list of common elements in all the sublists
    '''
    sets = [set(x) for x in input_list]
    common = reduce(lambda x, y : x & y,sets)
    return list(common)

if __name__ == "__main__":
    input_list = [
        [2,3,6,7],
        [2,3,8,9],
        [2,3]
    ]

    common_elements = findCommon(input_list)
    print(common_elements)