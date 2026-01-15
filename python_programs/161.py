'''
Write a function to remove all elements from a given list present in another list.
'''

def remove_all_elements_from_list(list1: list[int], list2: list[int]) -> list[int]:
    '''
    Takes two list as input and remove all the elements from list1 if they are present in list2
        Parameters:
            list1: list of integers containing all the elements
            list2: list of integers which need to be removed from list1
        Returns:
            A list after removing all the elements from list1 if they are present in list2
        Raises:
            Exception("Function expect list1 it should not be empty")
    '''
    if not list1:
        raise Exception("Function expect list1 it should not be empty")
    if not list2:
        return list1
    
    for ele in list1:
        if ele in list2:
            list1.remove(ele)
    return list1

if __name__ == "__main__":
    try:
        list1 = [1, 2, 3, 4 , 5, 2, 3, 5, 1, 7]
        list2 = [2, 7]
        resultList = remove_all_elements_from_list(list1, list2)
        print(resultList) # [1, 3, 4, 5, 3, 5, 1 ]

        list1 = [1, 2, 3, 4 , 5, 2, 3, 5, 1, 7]
        list2 = []
        resultList = remove_all_elements_from_list(list1, list2)
        print(resultList) # [1, 2, 3, 4 , 5, 2, 3, 5, 1, 7]

        list1 = []
        list2 = []
        resultList = remove_all_elements_from_list(list1, list2)
        print(resultList) # None
    except Exception as e:
        print(e)