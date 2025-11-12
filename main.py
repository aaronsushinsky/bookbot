from stats import get_word_count, get_character_count, get_sorted_letters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        words = f.read()
        total_words = get_word_count(words)
    return total_words

def main (filepath):
    num_words = get_book_text(filepath)
    num_letters = get_character_count(filepath)
    sorted_letters = get_sorted_letters(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
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

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len(sys.argv) > 1:   
    main(sys.argv[1])    