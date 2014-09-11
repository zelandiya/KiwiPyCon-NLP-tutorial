__author__ = 'a_medelyan'

# Goal: Learn about part of speech tagging
# Filter out words of irrelevant parts of speech
# http://www.nltk.org/book/ch05.html

import nltk
from nltk.corpus import movie_reviews
from nltk.probability import FreqDist

words = movie_reviews.words('pos/cv000_29590.txt')

# POS tag words

# Strip words from words that aren't nouns or adjectives

# Print stripped words

# Print most frequent words

# Spare time? Compare the most frequent words in both sets, while ignoring stopwords
# Caution (It will run for 1h on the entire movie reviews dataset, so use a subset)