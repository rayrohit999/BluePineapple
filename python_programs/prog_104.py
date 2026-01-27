def sortSublist(input_list : list[list[str]]) -> list[list[str]] :
    #sorting will be based on first word of list 
    result = [sorted(subList, key=lambda x: x[0]) for subList in input_list]
    return result


if __name__ == "__main__":
    input_list = [["Orange", "Yellow"], ["Apple", "Mango"], ["Car", "Bus"]]
    sorted_list = sortSublist(input_list) 
    print(sorted_list) #[['Orange', 'Yellow'], ['Apple', 'Mango'], ['Bus', 'Car']]

    input_list = [["Orange", "Yellow", "Aqua"], ["Apple", "Mango", "Pineapple"], ["Car", "Bus", "Plane"]]
    sorted_list = sortSublist(input_list)
    print(sorted_list) #[['Aqua', 'Orange', 'Yellow'], ['Apple', 'Mango', 'Pineapple'], ['Bus', 'Car', 'Plane']]

    input_list = [[]]
    sorted_list = sortSublist(input_list)
    print(sorted_list) # [[]]

    input_list = [["Aqua", "Apple", "Aqua"]]
    sorted_list = sortSublist(input_list)
    print(sorted_list)

