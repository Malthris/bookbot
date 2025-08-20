def string_to_words(full_book):
    word_counter = 0
    words = full_book.split()
    for word in words:
        word_counter += 1
    return word_counter

def count_letters(full_book):
    letter_count = {}

    lower_full_book = full_book.lower()
    
    for char in lower_full_book:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    
    return letter_count

def sort_on(items):
    return items["num"]

def sorted_list(counted_letters):
    list_of_letter = []

    for letter in counted_letters:
        list_of_letter.append({"char": letter, "num": counted_letters[letter]})
        #print(letter)

    list_of_letter.sort(reverse=True, key=sort_on)
    #print(list_of_letter)

    return list_of_letter
