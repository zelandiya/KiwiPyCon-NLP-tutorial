__author__ = 'a_medelyan'

# Goal: Extract ngrams, or multi-word phrases

from nltk.util import ngrams
from nltk.corpus import movie_reviews
from nltk.probability import FreqDist
from nltk.corpus import stopwords

words = movie_reviews.words('pos/cv000_29590.txt')

# What are the n-grams (from 2 to 5 words)?

# What are the most frequent ones?

# How do we filter out ngrams that aren't meaningful?
stop = stopwords.words('english')
boundaries = ['(', ')', '.', ',', ';', ':']


def acceptable(word):
    if word.lower() in stop:
        return False
    elif not word[0].isalpha():
        return False
    return True


def has_no_boundaries(my_gram):
    for my_word in my_gram:
        if my_word in boundaries:
            return False
    return True