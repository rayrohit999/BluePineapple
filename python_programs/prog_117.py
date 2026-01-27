from typing import Any
def convertToFloat(dataList: list[Any]) -> list[Any]:
    '''
    Convert all possible element of the list to float.
        Parameters:
            dataList(list): The input list containing elements of various types
        Returns:
            A new list with conveted elements to float if they are compatible 
    '''
    result = []
    for item in dataList:
        try:
            result.append(float(item))
        except (TypeError,ValueError) as e:
            result.append(item)
    return result

if __name__ == "__main__":
    dataList = ["13.4", 3, 15.3, "5", "car", [1, 2]]
    convertedList = convertToFloat(dataList)
    print(convertedList)