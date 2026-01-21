'''
Write a function to convert a tuple of string values to a tuple of integer values.
'''

def convert_string_tuple_to_integer(string_tup: tuple[str, ...]) -> tuple[int, ...]:
    '''
    Takes tuple of string as input and returns a tuple of integers
        Parameter:
            string_tup(tuple): Tuple of strings. it contains integers in from of string
        Returns:
            A tuple containg converted integers
        Raises:
            ValueError: If tuple contains a element which can't be converted to integer
            TypeError: If input is not a tuple
    '''
    if not string_tup:
        raise TypeError
    result = []
    for ele in string_tup:
        result.append(int(ele))

    return tuple(result)

if __name__ == "__main__":
    try:
        string_tup = ("12", "15", "234")
        int_tup = convert_string_tuple_to_integer(string_tup) # (12, 15, 234)
        print(int_tup)

        string_tup = ("12", "15", "234", "rohit")
        int_tup = convert_string_tuple_to_integer(string_tup) # Error
        print(int_tup)

        string_tup = ()
        int_tup = convert_string_tuple_to_integer(string_tup) # Error
        print(int_tup)
    except ValueError:
        print("Error: function expect tuple with only integer value")
    except TypeError:
        print("Error: input tuple can't be empty")
    except Exception as e:
        print(e)