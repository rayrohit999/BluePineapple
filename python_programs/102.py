def snake_to_camel(string: str) -> str:
    if not isinstance(string, str):
        return "Input should be a string only"

    i = 0
    while i < len(string):
        if string[i] == "_":
            string = string[:i] + string[i+1].upper() + string[i+2:]
        else:
            i += 1
    return string

if __name__ == "__main__":
    print(snake_to_camel("rohit_kumar_blue_pine_apple"))