""" Utilites """


def is_only_non_letters(word):
    for letter in word:
        if letter.isalpha():
            return False
    return True
