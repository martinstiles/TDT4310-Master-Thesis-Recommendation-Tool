""" Utilites """
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from textblob import TextBlob
import time
import re

TITLE_INDEX = 0
URL_INDEX = 4
DESCRIPTION_INDEX = 5
STOPWORDS_EN = set(stopwords.words('english'))
STOPWORDS_NO = set(stopwords.words('norwegian'))


def get_id_from_url(url):
    return url.split("=")[-1]


def get_thesis_id(obj):
    url = obj[URL_INDEX]
    return get_id_from_url(url)


def get_titles(objects):
    return [obj[TITLE_INDEX] for obj in objects]


def get_descriptions(objects):
    return [obj[DESCRIPTION_INDEX] for obj in objects]


def remove_square_brackets(string):
    return re.sub("[\[\]]", "", string)


def remove_feks(desctriptions):
    """
    Removes the abbreviation 'f.eks.' because it ruins the sent_tokenizer.
    Could possibly be more of such words.
    """
    return [re.sub(r'f.eks.', 'for eksempel', desctription) for desctription in desctriptions]


def is_only_non_letters(word):
    """ Returns True if the word only contains non-letter characters """
    for letter in word:
        if letter.isalpha():
            return False
    return True




def get_sentences(descriptions):
    """ Returns a 2D array with the sentences of each thesis """
    return [sent_tokenize(description) for description in descriptions]


def remove_space_coding(sentences):
    """ Remove '\xa0' from every sentence """
    return [re.sub(r'\xa0', ' ', sentence) for sentence in sentences]


def tokenize_sentences(sentences):
    return [word_tokenize(sentence) for sentence in sentences]


def remove_non_letter_tokens(tokens):
    """
    Removes non-letter tokens from an array,
    meaning it removes stuff like "," and ".", but keeps "debug-mode" etc.
    """
    return [token for token in tokens if not is_only_non_letters(token)]


def remove_non_letter_tokens_sentences(sentences_tokenized):
    """
    Removes non-letter tokens, meaning it removes stuff like "," and ".",
    but keeps "debug-mode" etc.
    """
    sentences = []
    for sentence in sentences_tokenized:
        sentences.append(remove_non_letter_tokens(sentence))
    return sentences


def make_lowercase(tokens):
    """ Makes every word in an array lower case """
    return [token.lower() for token in tokens]


def make_lowercase_sentences(sentences_tokenized):
    """ Makes every token in every sentence lowercase """
    sentences = []
    for sentence in sentences_tokenized:
        sentences.append(make_lowercase(sentence))
    return sentences


def remove_stopwords(tokens):
    """ Removes both English and Norwegian stopwords from an array of words """
    return [token for token in tokens if token not in STOPWORDS_EN and token not in STOPWORDS_NO]


def remove_stopwords_sentences(sentences_tokenized):
    """ Removes stopwords from an array of sentences """
    sentences = []
    for sentence in sentences_tokenized:
        sentences.append(remove_stopwords(sentence))
    return sentences


def get_language_tag(obj):
    """
    Returns a language tag based on the description text.
    Textblob provides good enough langauge detection to find only "en" and "no" for our data.
    """
    description = obj[DESCRIPTION_INDEX]
    blob = TextBlob(description)
    time.sleep(5)
    return blob.detect_language()
    
