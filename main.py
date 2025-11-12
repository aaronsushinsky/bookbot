def get_book_text(filepath):
    with open(filepath) as f:
        words = f.read()
        total = get_word_count(words)
    return total

def get_word_count(text):
    new_words = text.split()
    counter = 0
    for word in new_words:
        counter += 1
    return counter
    
def main ():
    num_words = get_book_text("books/frankenstein.txt")
    print(f'Found {num_words} total words')

main()    