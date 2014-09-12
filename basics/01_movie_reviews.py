__author__ = 'a_medelyan'

# Goal: Get movie reviews and read them
# See: http://www.nltk.org/book/ch02.html

from nltk.corpus import movie_reviews

# How many documents in this corpus?
print len(movie_reviews.fileids())

# What are the categories?
print movie_reviews.categories()

# What are some files names?
print movie_reviews.fileids('neg')[:10]
print movie_reviews.fileids('pos')[:10]

# Print the words in a sample text
print movie_reviews.words('pos/cv000_29590.txt')

# Print the original text
print movie_reviews.raw('pos/cv000_29590.txt')

# Print the sentences of the text
print movie_reviews.sents('pos/cv000_29590.txt')

# Spare time? Calculate the average number of words and sentences in positive and negative reviews
# Do people use a lot more words when giving positive vs. negative reviews?