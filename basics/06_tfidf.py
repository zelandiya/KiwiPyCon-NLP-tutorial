__author__ = 'a_medelyan'

# Goal: Learn TFxIDF scoring
from nltk.corpus import movie_reviews
from gensim import corpora, models

texts = []
for fileid in movie_reviews.fileids():
    words = movie_reviews.words(fileid)
    texts.append(words)

# Create dictionary, corpus and tfidf object using Gensim

# Compute IDF values for these words
# ['film', 'movie', 'comedy', 'violence', 'jolie']

# Spare time? Write a function that filters words based on their tfidf scores