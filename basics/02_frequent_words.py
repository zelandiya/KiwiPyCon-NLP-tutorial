__author__ = 'a_medelyan'

# Goal: Find out how to compute most frequent words using NLTK
# See: http://www.nltk.org/book/ch02.html

from nltk.corpus import movie_reviews
from nltk.probability import FreqDist

words = movie_reviews.words('pos/cv000_29590.txt')
words_by_frequency = FreqDist(words)

print 'Most frequent words in review'
# Depending on the NLTK version this will print either
# the most frequent or a random set of 20
print words_by_frequency.items()[:20]

# Compare the most frequent words in both sets
print ''
for category in movie_reviews.categories():

    print 'Category', category
    all_words = movie_reviews.words(categories=category)
    all_words_by_frequency = FreqDist(all_words)
    print all_words_by_frequency.items()[:20]

# expect roughly the same output!

# Spare time? Calculate the first 20 most frequent words for each category that are unique to that category
