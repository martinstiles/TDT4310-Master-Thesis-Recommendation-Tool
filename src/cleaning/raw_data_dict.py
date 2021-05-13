"""
To make it easier in future steps we want to save the 
raw data from the data retrieval step in a more convenient way:
as a dictionary with the thesis ID as key.
saved dictionary format:
{
    thesis_id: {
        "title": title,
        "description": sentences[]
    }
}
"""

from utils import *
from cleaner import get_thesis_ids
import json

TITLE_INDEX = 0
URL_INDEX = 4
DESCRIPTION_INDEX = 5


def load_data():
    with open("src/scraping/data.json") as file:
        data = json.load(file)["data"]
    return data


def get_dictionary(thesis_ids, titles, descriptions):
    """ Applies necessary methods and creates a dictionary """
    descriptions = remove_feks(descriptions)
    descriptions = get_sentences(descriptions)

    dictionary = {}
    zipped_list = zip(thesis_ids, titles, descriptions)
    for thesis_id, title, description in zipped_list:
        dictionary[thesis_id] = {
            "title": title,
            "description": description
        }
    return dictionary


def save_dictionary(data):
    with open("src/cleaning/raw_data_dict.json", "w") as file:
        json.dump(data, file)



def main():
    objects = load_data()

    thesis_ids = get_thesis_ids(objects)
    titles = get_titles(objects)
    descriptions = get_descriptions(objects)

    dictionary = get_dictionary(thesis_ids, titles, descriptions)
    
    save_dictionary(dictionary)


if __name__ == "__main__":
    main()