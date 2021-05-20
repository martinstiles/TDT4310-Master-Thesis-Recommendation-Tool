"""
Summarization algorithm:
--> Finds the two most important sentences by using the sum the tf-idf weight of each token in a sentence
--> Also creates a list of the most important words using the tf-idf weight
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import json


CLEANED_TITLE_INDEX = 0
CLEANED_DESCRIPTION_INDEX = 1


def load_data_dict():
    with open("src/cleaning/data_dict.json") as file:
        data = json.load(file)
    return data


def load_cleaned_data():
    with open("src/cleaning/cleaned_data.json") as file:
        cleaned_data = json.load(file)
    return cleaned_data


def get_cleaned_sentences_as_strings(cleaned_title, cleaned_description):
    """ Combines the title with the desciption sentences and makes every sentence into a string """
    sentences_as_tokens = [cleaned_title] + cleaned_description
    sentences_as_strings = [" ".join(sentence_tokens) for sentence_tokens in sentences_as_tokens]
    return sentences_as_strings


def get_weighted_sums(tfidf_vectors, num_vectors):
    weighted_sums = []
    for i in range(num_vectors):
        vector = tfidf_vectors[i].T.todense()
        weighted_sum = sum(vector)
        weighted_sums.append(weighted_sum)
    return weighted_sums


def get_index_of_most_important_sentences(weighted_sums, num_vectors):
    """ Finds and returns the index of the two sentences with the highest weighted sum """
    largest_sum_index, second_largest_sum_index = 0, 0
    largest_sum, second_largest_sum = 0, 0
    for i in range(num_vectors):
        current_sum = weighted_sums[i]
        if current_sum > largest_sum:
            largest_sum = current_sum
            largest_sum_index = i
        elif current_sum > second_largest_sum:
            second_largest_sum = current_sum
            second_largest_sum_index = i
    
    return largest_sum_index, second_largest_sum_index


def get_all_raw_sentences(thesis_id, raw_objects):
    """ Combines the title as a list with the list in 'description' """
    thesis = raw_objects[thesis_id]
    return [thesis["title"]] + thesis["description"]


def get_key_words(tfidf_vectorizer, tfidf_vectors):
    feature_names = tfidf_vectorizer.get_feature_names()
    important_words = []
    tfidf_matrix = tfidf_vectors.toarray()
    for row in tfidf_matrix:
        for i in range(len(row)):
            tfidf_value = row[i]
            if tfidf_value > 0.1:
                important_words.append((feature_names[i], tfidf_value))
    
    five_most_important_words = sorted(important_words, key=lambda tup: tup[1], reverse=True)[:5]
    key_words = [word for word, tfidf_value in five_most_important_words]
    return key_words


def get_summary(tfidf_vectors, thesis_id, raw_objects):
    num_vectors = tfidf_vectors.shape[0]

    # Find all weighted sums
    weighted_sums = get_weighted_sums(tfidf_vectors, num_vectors)

    # Find the two largest weighted_sums -> the two most important sentences
    first_index, second_index = get_index_of_most_important_sentences(weighted_sums, num_vectors)

    # We want the first index to be smallest (to get sentences in chronological order)
    if first_index > second_index:
        first_index, second_index = second_index, first_index
    
    all_raw_sentences = get_all_raw_sentences(thesis_id, raw_objects)

    summary = all_raw_sentences[first_index] + " " + all_raw_sentences[second_index]

    return summary


def get_thesis_summary_and_key_words(thesis_id, cleaned_title, cleaned_description, raw_objects):
    """
    Summary and key word generation happens in the same function so that we don't have to
    fit and transform the TF-IDF vectorizer multiple times.

    Creates a summary for the thesis by finding the weighted TF-IDF sum of the cleaned
    sentences and choses the heighest weighted sentences. The chosen sentences are mapped
    back to the original (raw) sentence.
    """
    cleaned_sentences_as_strings = get_cleaned_sentences_as_strings(cleaned_title, cleaned_description)

    tfidf_vectorizer = TfidfVectorizer(use_idf=True)
    tfidf_vectors = tfidf_vectorizer.fit_transform(cleaned_sentences_as_strings)

    # Generate the key words
    key_words = get_key_words(tfidf_vectorizer, tfidf_vectors)
    summary = get_summary(tfidf_vectors, thesis_id, raw_objects)

    return summary, key_words


def get_summaries(raw_objects, cleaned_objects, start=0, end=10):
    """ Finds the summary for every thesis one by one """
    summaries = {}
    c = 1
    for thesis_id, obj in cleaned_objects.items():
        if c < start:
            c += 1
            continue
        cleaned_title, cleaned_description = obj[CLEANED_TITLE_INDEX], obj[CLEANED_DESCRIPTION_INDEX]

        summary, key_words = get_thesis_summary_and_key_words(thesis_id, cleaned_title, cleaned_description, raw_objects)
        summaries[thesis_id] = {
            "summary": summary,
            "key_words": key_words
        }
        if c >= end:
            break
        c += 1
    return summaries


def summarizer(start, end):
    """ Returns a summary and the most important words for every thesis  """
    raw_objects = load_data_dict()
    cleaned_objects = load_cleaned_data()
    summaries = get_summaries(raw_objects, cleaned_objects, start, end)

    for key, value in summaries.items():
        print(key)
        print(value["summary"])
        print(value["key_words"])
        print("")



if __name__ == "__main__":
    start = 10
    end = 20
    summarizer(start, end)