from stats import string_to_words
from stats import count_letters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("/home/malthris/bootdev/projects/bookbot/books/frankenstein.txt")
    number_of_words = string_to_words(book_text)
    print(number_of_words, "words found in the document")
    number_per_letter = count_letters(book_text)
    print(number_per_letter)
main()