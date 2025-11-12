
def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    with open(text) as f:
        words = f.read()
        letter_count = {}
        for letter in words:
            letter = str.lower(letter)
            if letter in letter_count:
                newnum = letter_count[letter]
                letter_count[letter] = newnum + 1
            elif letter not in letter_count:
                letter_count[letter] = 1     
        return letter_count

def get_sorted_letters(dictionary):
    sorted_dictionary = []
    for key in dictionary:
        mini_dict = {}
        mini_dict["char"] = key
        mini_dict["num"] = dictionary[key]    
        sorted_dictionary.append(mini_dict)
        sorted_dictionary.sort(reverse=True, key=sort_function)
    return sorted_dictionary


def sort_function(new_list):
    return new_list["num"]