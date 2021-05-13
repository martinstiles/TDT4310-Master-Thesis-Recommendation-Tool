import nltk
# from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# from sklearn import svm
# import csv
# import pydantic.json
# from nltk.tokenize import word_tokenize
# import re
# from sklearn.model_selection import train_test_split
# from tabulate import tabulate
from stemmer import get_stemmed_descriptions
import json
from itertools import chain


def load_data():
    with open("../cleaning/stemmed_data.json") as file:
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


def main():
    # stemmer
    objects = load_data()
    english_theses, norwegian_theses = split_theses_on_language(objects)

    # We split the dataset 50/50
    # X_train, X_test, y_train, y_test = train_test_split(
    #     cleaned_texts, labels, test_size=0.5, random_state=420)

    # # Then we fit and vectorize the training set with TF-IDF representation
    vectorizer = TfidfVectorizer()
    english_terms = [" ".join(thesis) for thesis in english_theses.values()]
    english_tfs = vectorizer.fit_transform(english_terms)
    # print(english_tfs[0:1])
    test_query = vectorizer.transform(["nlp machine learning"])
    # print("\ntest_query:")
    # print(test_query)
    cosine_similarities = linear_kernel(test_query, english_tfs).flatten()
    print(cosine_similarities)
    related_docs_indices = cosine_similarities.argsort()[:-5:-1]
    print(related_docs_indices)
    print(cosine_similarities[related_docs_indices])
    print(english_tfs[0])
    # print(vectorizer.get_feature_names())

    # # We then train a SVM on the vectorized data
    # svc = svm.SVC(C=1000, probability=True)
    # svc.fit(X_train, y_train)

    # Finally, we evaluate the performance
    #

    # y_pred = svc.predict(X_test_vectorized)

    # # We then try to predict the probability that
    # # the test tweets were written by Trump or Musk
    # probabilities = svc.predict_proba(X_test_vectorized)

    # print("Prediction of which account wrote each tweet")
    # for i in range(len(probabilities[:10])):
    #     print("\nTweet:", (X_test[i]))
    #     print(
    #         f"Trump: {probabilities[i][0]:.6f} | Musk: {probabilities[i][1]:.6f}")

    # # Finally, we have the confusion matrix
    # conf = confusion_matrix(y_test, y_pred)
    # print("Confusion matrix:\n", conf)

    # # And the Precision and Recall of the Trump tweet predictions
    # print(f"\nPrecision: {conf[0][0] / (conf[0][0] + conf[1][0]):.6f}")
    # print(f"Recall: {conf[0][0] / (conf[0][0] + conf[0][1]):.6f}")
    pass


if __name__ == "__main__":
    main()
