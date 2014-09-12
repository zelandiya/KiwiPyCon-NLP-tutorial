__author__ = 'a_medelyan'

# Goal: Learn how to run classification and evaluating a classification algorithm
# http://www.nltk.org/book/ch06.html

from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
import random
import nltk

# Create classification data
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Create a set of features
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# Convert each document into a vector
featuresets = [(document_features(d), c) for (d,c) in documents]

# Experimental data
train_set, test_set = featuresets[1000:], featuresets[:1000]

# Train the classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Test the classifier's accuracy on test data
print(nltk.classify.accuracy(classifier, test_set))

# Test this approach on some new movies reviews
# from http://www.imdb.com/title/tt2209764/reviews?ref_=tt_urv
transcendence = ['../data/transcendence_1star.txt', '../data/transcendence_5star.txt', '../data/transcendence_8star.txt',
                 '../data/transcendence_great.txt']

# Re-train classifier on all documents
classifier = nltk.NaiveBayesClassifier.train(featuresets)

for review in transcendence:
    f = open(review)
    raw = f.read()
    document = word_tokenize(raw)
    features = document_features(document)
    print review, classifier.classify(features)