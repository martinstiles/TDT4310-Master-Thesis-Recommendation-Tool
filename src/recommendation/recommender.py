from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from stemmer import stem
import json


def load_stemmed_data():
    with open("src/cleaning/stemmed_data.json") as file:
        data = json.load(file)
    return data


def load_data_dict():
    with open("src/cleaning/data_dict.json") as file:
        data = json.load(file)
    return data


def get_theses_in_language(objects, language_tag):
    theses = {}
    for key, obj in objects.items():
        if obj[1] == language_tag:
            theses[key] = obj[0]
    return theses


def get_prepared_query(query, language_tag):
    return " ".join([stem(token.lower(), language_tag) for token in query.split()])


def get_tf_idf_cosine_similarity(vectorizer, docs_tfidf, query):
    query_tfidf = vectorizer.transform([query])
    cosine_similarities = cosine_similarity(query_tfidf, docs_tfidf).flatten()
    return cosine_similarities


def get_index_and_similarity_of_relevant_docs(cosine_similarities):
    index_of_relevant_docs = []
    similarities = []
    for i in range(cosine_similarities.shape[0]):
        cos_sim = cosine_similarities[i]
        index_of_relevant_docs.append(i)
        similarities.append(cos_sim)
        # if cos_sim > 0:
        #     index_of_relevant_docs.append(i)
        #     similarities.append(cos_sim)
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


def recommender(query, language_tag="en", n=5, eval_subset=None, debug=False):
    raw_objects = load_data_dict()

    # stemmer
    objects = load_stemmed_data()
    if eval_subset:  # For evaluation we want to use a subset provided in the input parameters
        objects = eval_subset

    theses = get_theses_in_language(objects, language_tag)

    # Fit and vectorize the training set with TF-IDF representation
    vectorizer = TfidfVectorizer()
    terms = [" ".join(thesis) for thesis in theses.values()]
    docs_tfidf = vectorizer.fit_transform(terms)

    prepared_query = get_prepared_query(query, language_tag)

    # Find similarities
    cosine_similarities = get_tf_idf_cosine_similarity(
        vectorizer, docs_tfidf, prepared_query)
    index_of_relevant_docs, similarities = get_index_and_similarity_of_relevant_docs(
        cosine_similarities)
    thesis_id_of_relevant_docs = get_thesis_id_of_relevant_docs(
        index_of_relevant_docs, theses)

    n_most_relevant_thesis_ids = get_n_most_relevant_thesis_ids(
        thesis_id_of_relevant_docs, similarities, n)

    n_most_relevant_theses = [get_thesis_object(thesis_id, raw_objects) for thesis_id in n_most_relevant_thesis_ids]

    if debug:
        for obj in n_most_relevant_theses:
            print(obj["id"])
            print(obj["title"])
            print("")
    
    return n_most_relevant_theses


if __name__ == "__main__":
    # "matlab Facial Recognition C++"  # "nlp music creativity"
    # "blockchain " # "energy efficieny" # "climate change"
    test_query = "nlp analysis games chatbot"
    recommender(test_query, language_tag="en", n=15, debug=True)
