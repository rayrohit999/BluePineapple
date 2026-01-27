def isAllDictionaryEmpty(dictList: list[dict]) -> bool:
    '''
    Takes a list of dictionaries and returns true if all the dictionaries are empty other wise false
        Parameters:
            dicList(list): list of dictionaries
        Returns:
            isEmpty(boolen): weather all dictionaries are empty or not. True if empty else False
    '''
    if not dictList:
        raise Exception("List can't be empty")
    isEmpty = True
    for x in dictList:
        if x:
            isEmpty = False
    return isEmpty

if __name__ == "__main__":
    try:
        dictList = [
            {},
            {},
            {},
        ]
        print(isAllDictionaryEmpty(dictList))

        dictList = [
            {},
            {},
            {"name" : "rohit"},
        ]
        print(isAllDictionaryEmpty(dictList))
        print(isAllDictionaryEmpty([]))
    except Exception as e:
        print(e)