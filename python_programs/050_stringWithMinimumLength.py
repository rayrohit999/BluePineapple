def string_with_minimum_length(stringList):
    minString = min(stringList,key = lambda i : len(i))
    return minString

if __name__ == "__main__":
    print(string_with_minimum_length(["rohit","mohit","aniket","utkarsh","ram","shyam",""])) # ""
    print(string_with_minimum_length(["rohit","mohit","aniket","utkarsh","ram","shyam"])) # "ram"
    print(string_with_minimum_length(["rohit","mohit","aniket","utkarsh","shyam"])) # "rohit"

