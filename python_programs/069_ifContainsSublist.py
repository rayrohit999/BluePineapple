def isContainSublist(main_list,sub_list):
    if not main_list or not sub_list:
        return "list should not be empty"
    
    if len(main_list) < len(sub_list):
        return False
    
    for i in range(len(main_list)):
        if main_list[i] == sub_list[0] and len(main_list)-i >= len(sub_list) and main_list[i:i+len(sub_list)] == sub_list:
            return True
    return False


    
if __name__ == "__main__":
    main_list = [1, 2, 3, 4, 5]
    sub_list  = [3, 4]
    print(isContainSublist(main_list,sub_list)) #True
    main_list = [1, 2, 3, 4, 5]
    sub_list  = [4, 3]
    print(isContainSublist(main_list,sub_list)) #False
    main_list = [1, 2, 3, 4, 5]
    sub_list  = [2, 4]
    print(isContainSublist(main_list,sub_list)) #False
    main_list = [1, 2, 3]
    sub_list  = [1, 2, 3]
    print(isContainSublist(main_list,sub_list)) #True
    main_list = [1, 2]
    sub_list  = [1, 2, 3]
    print(isContainSublist(main_list,sub_list)) #False
    

