def check_if_all_numbers_are_different(arr):
    status = len(arr) == len(set(arr))
    return "Yes" if status else "No"
print(check_if_all_numbers_are_different([1,2,3,4,5,6,7,8])) #yes
print(check_if_all_numbers_are_different([1,2,3,4,5,6,7,4,8])) #No
print(check_if_all_numbers_are_different([])) #yes

