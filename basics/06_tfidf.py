__author__ = 'a_medelyan'

# Goal: Learn TFxIDF scoring
import nltk
from nltk.corpus import movie_reviews
from nltk.probability import FreqDist
from gensim import corpora, models
import operator

texts = []

for fileid in movie_reviews.fileids():
    words = movie_reviews.words(fileid)
    texts.append(words)

dictionary = corpora.Dictionary(texts)

corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)

# IDF values
for word in ['film', 'movie', 'comedy', 'violence', 'jolie']:
    id = dictionary.token2id.get(word)
    if id:
        print word, id, tfidf.idfs[id]

tfidf.save('../data/tfidf.model')

# Get filtered words
words = movie_reviews.words('pos/cv000_29590.txt')
pos = nltk.pos_tag(words)
filtered_words = [x[0] for x in pos if x[1] in ('NN', 'NNS' 'JJ') and len(x[0]) > 1]

frequencies = FreqDist(filtered_words)

print ''
print 'By frequency:', frequencies.items()[:20]

scores = {}

for word in set(filtered_words):
    tf = float(frequencies[word]) / len(filtered_words)
    my_id = dictionary.token2id.get(word)
    if my_id:
        idf = tfidf.idfs[my_id]
    else:
        idf = 0
    scores[word] = tf*idf

ranked_words = sorted(scores.iteritems(), key=operator.itemgetter(1), reverse = True)

print 'By TFxIDF:', ranked_words[:20]