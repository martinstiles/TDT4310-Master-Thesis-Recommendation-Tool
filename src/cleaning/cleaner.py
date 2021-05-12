"""
Pipeline for data cleaning. The resulting data from this process will be on the format:
{
    thesis_id:
        [
            cleaned_title,          # 2D array with every title as tokens
            cleaned_description,    # 3D array with description tokens on the format:
                                      descriptions[sentences[tokens[]]]
            language_tag,           # "en" or "no" to tag element with language
        ]
}
"""


from utils import *
import json


def load_data():
    with open("src/scraping/data.json") as file:
        data = json.load(file)["data"]
    return data


def save_cleaned_data(cleaned_data):
    with open("src/cleaning/cleaned_data.json", "w") as file:
        json.dump(cleaned_data, file)


def get_thesis_ids(objects):
    return [get_thesis_id(obj) for obj in objects]


def get_cleaned_titles(objects):
    """ Extract titles and perform cleaning """
    titles = get_titles(objects)
    titles = [remove_square_brackets(title) for title in titles]
    titles = [word_tokenize(title) for title in titles]
    titles = [remove_non_letter_tokens(title) for title in titles]
    titles = [make_lowercase(title) for title in titles]
    titles = [remove_stopwords(title) for title in titles]

    return titles


def get_cleaned_descriptions(objects):
    descriptions = get_descriptions(objects)

    # removing "f.eks." must be done here because it messes up get_sentences()
    descriptions = remove_feks(descriptions)

    # desc_sentences is a 2D array
    desc_sentences = get_sentences(descriptions)
    desc_sentences = [remove_space_coding(
        sentences) for sentences in desc_sentences]  # Necessary for summarizer -> The actual senteces that should be mapped to

    # desc_sentences_tokenized is a 3D array
    desc_sentences_tokenized = [tokenize_sentences(
        sentences) for sentences in desc_sentences]
    desc_sentences_tokenized = [remove_non_letter_tokens_sentences(
        sentences) for sentences in desc_sentences_tokenized]
    desc_sentences_tokenized = [make_lowercase_sentences(
        sentences) for sentences in desc_sentences_tokenized]
    desc_sentences_tokenized = [remove_stopwords_sentences(sentences_tokenized)
                                for sentences_tokenized in desc_sentences_tokenized]

    return desc_sentences_tokenized


def get_language_tags(objects):
    language_tags = []
    for i in range(len(objects)):
        language_tags.append(get_language_tag(objects[i]))
        print(i)

    return language_tags


def verify(data_size, thesis_ids, cleaned_titles, cleaned_descriptions, language_tags):
    assert len(thesis_ids) == data_size, "Not all ids found"
    assert len(cleaned_titles) == data_size, "Not all titles found"
    assert len(cleaned_descriptions) == data_size, "Not all descriptions found"
    assert len(language_tags) == data_size, "Not all language tags found"


def format_data(data_size, thesis_ids, cleaned_titles, cleaned_descriptions, language_tags):
    formatted_data = {}
    for i in range(data_size):
        formatted_data[thesis_ids[i]] = [
            cleaned_titles[i],
            cleaned_descriptions[i],
            language_tags[i]
        ]
    return formatted_data


def main():
    # Load objects and perform cleaning
    objects = load_data()
    thesis_ids = get_thesis_ids(objects)
    print("THESIS IDS DONE")
    cleaned_titles = get_cleaned_titles(objects)
    print("TITLES DONE")
    cleaned_descriptions = get_cleaned_descriptions(objects)
    print("DESCIPTIONS DONE")
    language_tags = get_language_tags(objects)

    # Verify that we have the data for all objects
    data_size = len(objects)
    verify(data_size, thesis_ids, cleaned_titles,
           cleaned_descriptions, language_tags)

    # Format the cleaned data and save it to json file
    cleaned_data = format_data(
        data_size, thesis_ids, cleaned_titles, cleaned_descriptions, language_tags)

    save_cleaned_data(cleaned_data)


if __name__ == "__main__":
    main()
