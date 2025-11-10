def get_book_text(filepath):
    with open(filepath) as f:
        words = f.read()
        new_words = words.split()
        counter = 0
        for word in new_words:
            #print(word, counter)
            counter += 1
    return counter

def main ():
    num_words = get_book_text("books/frankenstein.txt")
    print(f'Found {num_words} total words')



main()    