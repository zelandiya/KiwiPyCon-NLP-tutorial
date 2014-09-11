__author__ = 'a_medelyan'

# Goal: Learn how to perform topic modeling using Gensim

from gensim import corpora
from gensim import models
from nltk.corpus import movie_reviews
import basics_applied.keyword_extractor
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


candidate_extractor = basics_applied.keyword_extractor.CandidateExtractor()

for category in movie_reviews.categories():

    texts = []
    for fileid in movie_reviews.fileids(category):
        words = movie_reviews.words(fileid)
        clean_words = candidate_extractor.run(words, 2) # Experiment with removing ,1
        texts.append(clean_words)

    dictionary = corpora.Dictionary(texts)

    # Experiment with commenting this out or changing values
    dictionary.filter_extremes(no_below=10, no_above=0.1, keep_n=10000)

    corpus = [dictionary.doc2bow(text) for text in texts]

    print 'Category', category

    print 'LDA'
    lda = models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=10, passes=5)

    print 'HDP'
    model = models.hdpmodel.HdpModel(corpus, id2word=dictionary)
