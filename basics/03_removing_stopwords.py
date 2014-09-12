__author__ = 'a_medelyan'

# Goal: Removing stopwords
# See: http://www.nltk.org/book/ch02.html

from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from string import punctuation

stop = stopwords.words('english')

# Strip stopwords from text
words = movie_reviews.words('pos/cv000_29590.txt')
print words[:20]
no_stopwords = [word for word in words if word not in stop]
print no_stopwords[:20]

# Compare the most frequent words in both sets, while ignoring stopwords
print ''
for category in movie_reviews.categories():

    print 'Category', category
    all_words = [word for word in movie_reviews.words(categories=category)
                 if word not in stop and word[0] not in punctuation]
    all_words_by_frequency = FreqDist(all_words)
    print all_words_by_frequency.items()[:20]

# Spare time? Read in a different stopwords file and compare the results