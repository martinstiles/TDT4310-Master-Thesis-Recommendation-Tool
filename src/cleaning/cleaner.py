from utils import is_only_non_letters
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import json
import re

stop_words_en = set(stopwords.words('english'))
stop_words_no = set(stopwords.words('norwegian'))


def load_data():
    with open("src/scraper/data.json") as file:
        data = json.load(file)["data"]
    return data


def get_description(obj):
    return obj[6]


def get_descriptions(objects):
    return [get_description(obj) for obj in objects]


def remove_feks(desctriptions):
    """
    Removes the abbreviation 'f.eks.' because it ruins the sent_tokenizer.
    Could possibly be more of such words.
    """
    return [re.sub(r'f.eks.', 'for eksempel', desctription) for desctription in desctriptions]


def get_sentences(descriptions):
    """ Returns a 2D array with the sentences of each thesis """
    return [sent_tokenize(description) for description in descriptions]


def remove_space_coding(sentences):
    """ Remove '\xa0' from every sentence """
    return [re.sub(r'\xa0', ' ', sentence) for sentence in sentences]


def tokenize_sentence(sentences):
    return [word_tokenize(sentence) for sentence in sentences]


def remove_non_letter_tokens(sentences_tokenized):
    """
    Removes non-letter tokens, meaning it removes stuff like "," and ".",
    but keeps "debug-mode" etc.
    """
    sentences = []
    for sentence in sentences_tokenized:
        tokens = []
        for token in sentence:
            if is_only_non_letters(token):
                continue
            # Add other statements if necessary
            tokens.append(token)
        sentences.append(tokens)
    return sentences


def make_lowercase(sentences_tokenized):
    """ Makes every token in every sentence lowercase """
    sentences = []
    for sentence in sentences_tokenized:
        sentences.append([token.lower() for token in sentence])
    return sentences


def remove_stopwords(sentences_tokenized):
    """
    Removes both English and Norwegian stop words.
    We do not know the language of the desciption.
    """
    sentences = []
    for sentence in sentences_tokenized:
        tokens = []
        for token in sentence:
            if token not in stop_words_en and token not in stop_words_no:
                tokens.append(token)
        sentences.append(tokens)
    return sentences


"""
For summarizer: use sentences
For key words: don't use sentences (or maybe use sentences)
For recommendations: don't use sentences
--> Data cleaning will save data as sentences, but if not needed just
    flatten the array to 2D.
"""


def main():
    objects = load_data()
    # TODO: remove [x:y] ([8:9] -> norsk)
    descriptions = get_descriptions(objects)[8:9]
    # Must be called here because it messes up get_sentences
    descriptions = remove_feks(descriptions)

    # desc_sentences is a 2D array
    desc_sentences = get_sentences(descriptions)
    desc_sentences = [remove_space_coding(
        sentences) for sentences in desc_sentences]  # Necessary for summarizer -> The actual senteces that should be mapped to

    # desc_sentences_tokenized is a 3D array
    desc_sentences_tokenized = [tokenize_sentence(
        sentences) for sentences in desc_sentences]
    desc_sentences_tokenized = [remove_non_letter_tokens(
        sentences) for sentences in desc_sentences_tokenized]
    desc_sentences_tokenized = [make_lowercase(
        sentences) for sentences in desc_sentences_tokenized]
    desc_sentences_tokenized = [remove_stopwords(sentences_tokenized)
                                for sentences_tokenized in desc_sentences_tokenized]

    print(desc_sentences_tokenized)


if __name__ == "__main__":
    main()
