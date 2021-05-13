from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from stemmer import stem
import nltk
import json


def load_stemmed_data():
    with open("src/cleaning/stemmed_data.json") as file:
        data = json.load(file)
    return data


def load_cleaned_data():
    with open("src/cleaning/cleaned_data.json") as file:
        data = json.load(file)
    return data


def split_theses_on_language(objects):
    english_theses = {}
    norwegian_theses = {}
    for key, obj in objects.items():
        if obj[1] == "no":
            norwegian_theses[key] = obj[0]
        else:
            english_theses[key] = obj[0]
    return english_theses, norwegian_theses


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
        

def get_n_most_relevant_thesis_ids(thesis_id_of_relevant_docs, similarities):
    ids_and_similarities = zip(thesis_id_of_relevant_docs, similarities)
    n_most_relevant_thesis_ids = sorted(ids_and_similarities, key=lambda x: x[1], reverse=True)[:5]
    n_most_relevant_thesis_ids = [thesis_id for thesis_id, sim in n_most_relevant_thesis_ids]
    return n_most_relevant_thesis_ids


def main():
    # stemmer
    objects = load_stemmed_data()
    english_theses, norwegian_theses = split_theses_on_language(objects)

    # Then we fit and vectorize the training set with TF-IDF representation
    vectorizer = TfidfVectorizer()
    english_terms = [" ".join(thesis) for thesis in english_theses.values()]
    english_tfs = vectorizer.fit_transform(english_terms)

    test_query = "deep learning matlab"  # "matlab Facial Recognition C++"  # "nlp music creativity"
    test_query = " ".join([stem(token.lower()) for token in test_query.split()])

    cosine_similarities = get_tf_idf_cosine_similarity(vectorizer, english_tfs, test_query)
    index_of_relevant_docs, similarities = get_index_and_similarity_of_relevant_docs(cosine_similarities)
    thesis_id_of_relevant_docs = get_thesis_id_of_relevant_docs(index_of_relevant_docs, english_theses)

    n_most_relevant_thesis_ids = get_n_most_relevant_thesis_ids(thesis_id_of_relevant_docs, similarities)

    n_most_relevant_theses = [(objects[thesis_id], thesis_id) for thesis_id in n_most_relevant_thesis_ids]

    for tup in n_most_relevant_theses:
        print(tup[0])
        print("")



if __name__ == "__main__":
    main()
