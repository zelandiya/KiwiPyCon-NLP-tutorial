__author__ = 'a_medelyan'

# Goal: Learn about part of speech tagging
# Filter out words of irrelevant parts of speech
# http://www.nltk.org/book/ch05.html

import nltk
from nltk.corpus import movie_reviews
from nltk.probability import FreqDist
from time import gmtime, strftime

# Test part of speech tagging
words = movie_reviews.words('pos/cv000_29590.txt')
pos = nltk.pos_tag(words)
print pos

# Strip words from text that aren't nouns or adjectives
filtered_words = [x[0] for x in pos if x[1] in ('NN', 'JJ')]

print filtered_words
print FreqDist(filtered_words).items()[:20]

print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# Compare the most frequent words in both sets, while ignoring stopwords
print ''
for category in movie_reviews.categories():

    print 'Category', category
    all_words = movie_reviews.words(categories=category)[:1000]
    pos = nltk.pos_tag(all_words)
    all_filtered_words = [x[0] for x in pos if x[1] in ('NN', 'NNS', 'JJ') and len(x[0]) > 1]

    all_words_by_frequency = FreqDist(all_filtered_words)
    print all_words_by_frequency.items()[:20]

print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

