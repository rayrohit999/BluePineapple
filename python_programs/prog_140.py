'''
Write a function to extract elements that occur singly in the given tuple list.
'''

def singleOccurrence(tupples: list[tuple]) -> list:
    '''
    Takes list of tupples as input and returns the elements that
    occures only once across all the tuples.
        Parameter:
            tupples (list[tuple]): list of tuples
        Returns:
            (list): list of elements that occures once
        Raises:
            TypeError: If input is not list of tupples
    '''
    if not isinstance(tupples, list):
        raise TypeError
    
    if not all(isinstance(tup, tuple) for tup in tupples):
        raise TypeError
    
    result = []
    elements = []
    for tup in tupples:
        elements.extend(tup)
    for ele in elements:
        if elements.count(ele) == 1:
            result.append(ele)
    return result