import nltk
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import csv
import json
from nltk import stem
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from sklearn.model_selection import train_test_split
from tabulate import tabulate

nltk.download('stopwords')

# Creating stemmer and defining stop words
stemmer = stem.PorterStemmer()
stopwords = set(stopwords.words('english'))

# Reading in Elon Musk's tweets
content = []
with open('tweets/elonmusk_tweets.csv', newline='', encoding='latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        content.append(row[2])

# Extracting the text of the tweets and labeling them.
# Label = 1: tweet is written by "Musk"
texts = content
labels = [1 for row in content]

# Reading in Donald Trump's tweets
with open("tweets/realDonaldTrump.json", "r", encoding='latin-1') as jsonfile:
    tweet_objects = json.load(jsonfile)

# Extracting the text of the tweets and labeling them.
# Label = 0: tweet is written by "Trump"
texts = texts + [tweet["text"] for tweet in tweet_objects]
labels = labels + [0 for row in tweet_objects]

# Function for tokenizing, removing special characters and stemming the tokens


def text_cleaning(text):
    text = text.lower()
    text = " ".join([word for word in word_tokenize(text)
                     if not word in stopwords])
    text = re.sub(r"[!?:;\-,.<>@%(b?')]", r"", text)
    text = " ".join([stemmer.stem(word) for word in text.split()])
    return text


# Clean the tweets
cleaned_texts = list(map(text_cleaning, texts))

# print(texts[:10])
print(cleaned_texts[len(content) - 2:len(content) + 2])
print(labels[len(content) - 2:len(content) + 2])

# We split the dataset 50/50, as there are relatively few tweets from
# Musk (about 2800) out of the full number of tweets (almost 60000)
X_train, X_test, y_train, y_test = train_test_split(
    cleaned_texts, labels, test_size=0.5, random_state=420)


# Then we fit and vectorize the training set with TF-IDF representation
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)

# We then train a SVM on the vectorized data
svc = svm.SVC(C=1000, probability=True)
svc.fit(X_train, y_train)

# Finally, we evaluate the performance
X_test_vectorized = vectorizer.transform(X_test)
y_pred = svc.predict(X_test_vectorized)

# We then try to predict the probability that
# the test tweets were written by Trump or Musk
probabilities = svc.predict_proba(X_test_vectorized)

print("Prediction of which account wrote each tweet")
for i in range(len(probabilities[:10])):
    print("\nTweet:", (X_test[i]))
    print(
        f"Trump: {probabilities[i][0]:.6f} | Musk: {probabilities[i][1]:.6f}")

# Finally, we have the confusion matrix
conf = confusion_matrix(y_test, y_pred)
print("Confusion matrix:\n", conf)

# And the Precision and Recall of the Trump tweet predictions
print(f"\nPrecision: {conf[0][0] / (conf[0][0] + conf[1][0]):.6f}")
print(f"Recall: {conf[0][0] / (conf[0][0] + conf[0][1]):.6f}")
