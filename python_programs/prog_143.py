'''
Write a function to find number of lists present in the given tuple.
'''

def countLists(tup: tuple) -> int:
    '''
    Takes tuples as input and count number of list present as element of tuple
        Parameter:
            tup (tuple): input tuple
        Returns:
            (int): number of list present as element in input tuple
        Raises:
            TypeError: If input is not tupple
    '''
    if not isinstance(tup, tuple):
        raise TypeError
    if not tuple:
        return 0
    count = 0
    for ele in tup:
        if isinstance(ele, list):
            count += 1

    return count