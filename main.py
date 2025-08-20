import sys
from stats import string_to_words
from stats import count_letters
from stats import sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    number_of_words = string_to_words(book_text)
    
    number_per_letter = count_letters(book_text)
    #print(number_per_letter)
    number_list = sorted_list(number_per_letter)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", number_of_words, "total words")
    print("--------- Character Count -------")
    for i in range(0, len(number_list)-1):
        if number_list[i]["char"].isalpha():
            print(f"{number_list[i]["char"]}: {number_list[i]["num"]}")    
    print("============= END ===============")

main()