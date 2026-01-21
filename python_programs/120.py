'''
Write a function to find the maximum product from the pairs of tuples within a given list.
'''
def maxProduct(tuple_list: list[tuple[int, int]]) -> int :
    '''
    Takes list of tuples as input and find the max product from the pairs of tuples within that list
        Parameter:
            tuple_list(list[tuple(int, int)]): List of tuples
        Returns: 
            Maximum product from the pairs of tuples within a given list.
    '''
    if not tuple_list:
        raise Exception("Function except at least one element in input list, passed none")
    return max([abs(a * b) for a, b in tuple_list])

if __name__ == "__main__":
    try:
        tuple_list = [(2, 3), (3, 4), (10, 3), (6, 4)]
        print(maxProduct(tuple_list)) #30

        tuple_list = []
        print(maxProduct(tuple_list)) #30
    except Exception as e:
        print(e)