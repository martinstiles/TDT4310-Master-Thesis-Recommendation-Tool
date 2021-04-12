""" Utility file: defines common helper methods for the scraper code """


def remove_first_word_in_string(string):
    return " ".join(string.split()[1:])


def remove_last_word_in_string(string):
    return " ".join(string.split()[:1])
