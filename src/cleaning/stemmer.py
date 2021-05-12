""" Stemming must be performed after language tags has been found """

from nltk.stem.snowball import SnowballStemmer

SB_EN = SnowballStemmer('english')
SB_NO = SnowballStemmer('norwegian')


def stem(token, language_tag):  
    if language_tag == "no":
        return SB_NO.stem(token)
    return SB_EN.stem(token)


def load_data():
    # Load cleaned data
    pass


def get_stemmed_descriptions(cleaned_descriptions, language_tags):
    stemmed_descriptions = []
    for description, language_tag in zip(cleaned_descriptions, language_tags):
        sentences = []
        for sentence in description:
            sentences.append([stem(token, language_tag) for token in sentence])
        stemmed_descriptions.append(sentences)

    return stemmed_descriptions


def main():
    # cleaned_descriptions, language_tags = load_data()
    # stemmed_descriptions = get_stemmed_descriptions(cleaned_descriptions, language_tags)
    # Do something with it (save it / update data file)
    pass


if __name__ == "__main__":
    main()