def length_of_longest_word(paragraph: str) -> int:
    length = 0
    words = paragraph.split()
    for word in words:
        if len(word) > length:
            length = len(word)
    return length
if __name__ == "__main__":
    para = "Hello this is great oportunity to learn. you should foucs on learning by heart"
    print(length_of_longest_word(para))