__author__ = 'a_medelyan'

# Goal: Extract ngrams, or multi-word phrases

from nltk.util import ngrams
from nltk.corpus import movie_reviews
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from string import punctuation

words = movie_reviews.words('pos/cv000_29590.txt')

# What are most common n-grams?
my_ngrams = []
for n in range(2, 5):
    for gram in ngrams(words, n):
        phrase = ' '.join(gram)
        my_ngrams.append(phrase)

print 'Ngrams', my_ngrams[:25]
frequent4 = FreqDist(my_ngrams)
print 'Ngrams by freq', frequent4.items()[:25]



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


my_ngrams = []
for n in range(2, 5):
    for gram in ngrams(words, n):
        if acceptable(gram[0]) and acceptable(gram[-1]) and has_no_boundaries(gram):
            phrase = ' '.join(gram)
            my_ngrams.append(phrase)

print 'Clean Ngrams', my_ngrams[:25]
frequent4 = FreqDist(my_ngrams)
print 'Clean Ngrams by freq', frequent4.items()[:25]