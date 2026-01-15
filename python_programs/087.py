def merge(dict1 : dict, dict2 : dict , dict3 : dict) -> dict:
    dict1.update(dict2)
    dict1.update(dict3)
    return dict1

if __name__ == "__main__":
    dict1 = {"orange" : 5, "apple" : 12, "mango" : 10}
    dict2 = {"mango" : 12, "guava" : 13, "papaya" : 25}
    dict3 = {"orange" : 45, "apple" : 12, "mango" : 75, "pear" : 45}
    mergedDict = merge(dict1, dict2, dict3)
    print(mergedDict)