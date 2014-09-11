__author__ = 'a_medelyan'

# Goal: Find out how to compute most frequent words using NLTK
# See: http://www.nltk.org/book/ch02.html

from nltk.corpus import movie_reviews
from nltk.probability import FreqDist

words = movie_reviews.words('pos/cv000_29590.txt')

# Calculate how many times each word appears in the review

# Print out the most frequent 20 words and their counts

# Compare the most frequent words in positive and negative reviews

# Spare time? Calculate the first 20 most frequent words for each category that are unique to that category
