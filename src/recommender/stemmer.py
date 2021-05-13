""" Stemming must be performed after language tags has been found """

from nltk.stem.snowball import SnowballStemmer
import json

SB_EN = SnowballStemmer('english')
SB_NO = SnowballStemmer('norwegian')


def stem(token, language_tag="en"):
    if language_tag == "no":
        return SB_NO.stem(token)
    return SB_EN.stem(token)


def flatten(token_list):
    # print(token_list)
    flattened_list = []
    for sent in token_list:
        if sent:
            flattened_list += sent
    return flattened_list


def load_data():
    with open("src/cleaning/cleaned_data.json", 'r', encoding="utf-8") as file:
        objects = json.load(file)
        clean_descs = {key: obj[0] + flatten(obj[1])
                       for key, obj in objects.items()}
        language_tags = {key: obj[2] for key, obj in objects.items()}
    return clean_descs, language_tags


def save_data(stemmed_data):
    with open("src/cleaning/stemmed_data.json", "w") as file:
        json.dump(stemmed_data, file)


def get_stemmed_descriptions(cleaned_descriptions, language_tags):
    stemmed_descriptions = {}
    for key, description in cleaned_descriptions.items():
        stemmed_tokens = []
        for token in description:
            stemmed_tokens.append(stem(token, language_tags[key]))
        stemmed_descriptions[key] = [stemmed_tokens, language_tags[key]]
    return stemmed_descriptions


def main():
    cleaned_descriptions, language_tags = load_data()
    # Creating stemmer and defining stop words
    stemmed_descriptions = get_stemmed_descriptions(
        cleaned_descriptions, language_tags)
    # Do something with it (save it / update data file)
    save_data(stemmed_descriptions)


if __name__ == "__main__":
    main()
