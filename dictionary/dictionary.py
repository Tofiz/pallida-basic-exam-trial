word_dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(dictionary):
    hun_word = input("Type the hungarian word: ")
    eng_word = input("type it in english: ")
    dictionary.append({hun_word:eng_word})
    return dictionary

add_word(word_dictionary)
# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'
print(word_dictionary)

def translate_to_hun(eng_word):
    pass


def translate_to_eng(d):
    given_word = input("HUN to ENG dictionary: ")
    for k in d:
        if k in d.itervalues():
            print("ok")
        else:
            print(given_word)
translate_to_eng(word_dictionary)
