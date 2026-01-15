def odd_or_even_length(word : str) -> str:
    if not word:
        return "Emplty string"
    return "Even" if len(word) % 2 ==0 else "Odd"

if __name__ == "__main__":
    print(odd_or_even_length("rohit"))
    print(odd_or_even_length("rohi"))
    print(odd_or_even_length(""))