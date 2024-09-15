import sys

def main():
    path_to_file = "books/frankenstein.txt"
    text = print_text(path_to_file)
    numbers = number_of_words(text)
    print(text)
    print(f"The number of words in the book are: {numbers}")
    number_of_character(text)

def print_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    return len(text.split())

def number_of_character(text):
    lower_text = text.lower()
    characters_dict = {}
    sentence = []
    for letter in lower_text:
        if letter in characters_dict:
            characters_dict[letter] += 1
        else: 
            characters_dict[letter] = 1
    for char, count in characters_dict.items():
        sentence.append({"char": char, "count": count})
    for item in sentence:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['count']} times")
    print("End of list")
    

if __name__ == "__main__":
    main()


