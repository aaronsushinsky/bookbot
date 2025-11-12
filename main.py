from stats import get_word_count, get_character_count, get_sorted_letters

def get_book_text(filepath):
    with open(filepath) as f:
        words = f.read()
        total_words = get_word_count(words)
    return total_words

def main ():
    num_words = get_book_text("books/frankenstein.txt")
    num_letters = get_character_count("books/frankenstein.txt")
    sorted_letters = get_sorted_letters(num_letters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    for line in sorted_letters:
        checker = line["char"]
        if checker.isalpha() == True:
            print(f'{line["char"]}: {line["num"]}')
        else:
            pass
    print("============= END ===============")
main()    