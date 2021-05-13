from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from stemmer import stem
import nltk
import json


def load_stemmed_data():
    with open("src/cleaning/stemmed_data.json") as file:
        data = json.load(file)
    return data


def load_raw_data():
    with open("src/cleaning/raw_data_dict.json") as file:
        data = json.load(file)
    return data


def get_theses_in_language(objects, language_tag):
    theses = {}
    for key, obj in objects.items():
        if obj[1] == language_tag:
            theses[key] = obj[0]
    return theses


def get_prepared_query(query):
    return " ".join([stem(token.lower()) for token in query.split()])


def get_tf_idf_cosine_similarity(vectorizer, docs_tfidf, query):
    query_tfidf = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_tfidf, docs_tfidf).flatten()
    return cosine_similarities


def get_index_and_similarity_of_relevant_docs(cosine_similarities):
    index_of_relevant_docs = []
    similarities = []
    for i in range(cosine_similarities.shape[0]):
        cos_sim = cosine_similarities[i]
        if cos_sim > 0:
            index_of_relevant_docs.append(i)
            similarities.append(cos_sim)
    return index_of_relevant_docs, similarities


def get_thesis_id_of_relevant_docs(index_of_relevant_docs, english_theses):
    thesis_id_of_relevant_docs = []
    i = 0
    for thesis_id in english_theses:
        if i in index_of_relevant_docs:
            thesis_id_of_relevant_docs.append(thesis_id)
        i += 1
    return thesis_id_of_relevant_docs


def get_n_most_relevant_thesis_ids(thesis_id_of_relevant_docs, similarities, n=5):
    ids_and_similarities = zip(thesis_id_of_relevant_docs, similarities)
    n_most_relevant_thesis_ids = sorted(
        ids_and_similarities, key=lambda x: x[1], reverse=True)[:n]
    n_most_relevant_thesis_ids = [
        thesis_id for thesis_id, sim in n_most_relevant_thesis_ids]
    return n_most_relevant_thesis_ids


def get_thesis_object(thesis_id, raw_objects):
    thesis_object = {
        "title": raw_objects[thesis_id]["title"],
        "description": raw_objects[thesis_id]["description"],
        "id": thesis_id
    }
    return thesis_object


def recommender(query, language_tag="en"):
    raw_objects = load_raw_data()

    # stemmer
    objects = load_stemmed_data()
    theses = get_theses_in_language(objects, language_tag)

    # Then we fit and vectorize the training set with TF-IDF representation
    vectorizer = TfidfVectorizer()
    english_terms = [" ".join(thesis) for thesis in theses.values()]
    english_tfs = vectorizer.fit_transform(english_terms)

    prepared_query = get_prepared_query(query)

    # Find similarities
    cosine_similarities = get_tf_idf_cosine_similarity(
        vectorizer, english_tfs, test_query)
    index_of_relevant_docs, similarities = get_index_and_similarity_of_relevant_docs(
        cosine_similarities)
    thesis_id_of_relevant_docs = get_thesis_id_of_relevant_docs(
        index_of_relevant_docs, theses)

    n_most_relevant_thesis_ids = get_n_most_relevant_thesis_ids(
        thesis_id_of_relevant_docs, similarities)

    n_most_relevant_theses = [get_thesis_object(thesis_id, raw_objects) for thesis_id in n_most_relevant_thesis_ids]

    for obj in n_most_relevant_theses:
        print(obj["id"])
        print(obj["title"])
        print("")
    
    return n_most_relevant_theses


if __name__ == "__main__":
    # "matlab Facial Recognition C++"  # "nlp music creativity"
    # "blockchain " # "energy efficieny" # "climate change"
    test_query = "deep learning matlab"
    recommender(test_query, "en")
