from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        words = f.read()
        total = get_word_count(words)
    return total

def main ():
    num_words = get_book_text("books/frankenstein.txt")
    print(f'Found {num_words} total words')

main()    