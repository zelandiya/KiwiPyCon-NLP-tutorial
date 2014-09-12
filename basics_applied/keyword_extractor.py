__author__ = 'a_medelyan'

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import ngrams
from gensim import corpora, models
import operator


def acceptable(word, stop):
    if word.lower() in stop:
        return False
    elif not word[0].isalpha():
        return False
    return True


def has_no_boundaries(my_gram):
    for my_word in my_gram:
        if my_word in ['(', ')', '.', ',', ';', ':']:
            return False
    return True


def get_ngrams(my_words, stop, min_length=2, max_length=5):
    my_ngrams = []
    for n in range(min_length, max_length):
        for gram in ngrams(my_words, n):
            if acceptable(gram[0], stop) and acceptable(gram[-1], stop) and has_no_boundaries(gram):
                phrase = ' '.join(gram)
                my_ngrams.append(phrase)
    return my_ngrams


def get_candidates(words, stop):

    # more complex processing that requires more time
    # pos = nltk.pos_tag(words)
    # filtered_words = [x[0] for x in pos if x[1] in ('NN', 'NNS' 'JJ') and len(x[0]) > 1]

    filtered_words = [word for word in words if word not in stop and word[0].isalpha()]
    text_ngrams = get_ngrams(words, stop)
    return filtered_words + text_ngrams


class CandidateExtractor(object):

    def __init__(self):
        self.__stop = stopwords.words('english')

    def run(self,words, min_length=1):
        if min_length == 1:
            return get_candidates(words, self.__stop)
        else:
            return get_ngrams(words, self.__stop, min_length)

def get_tfidf(texts, dictionary):
    corpus = [dictionary.doc2bow(text) for text in texts]
    return models.TfidfModel(corpus)


def score_candidates(candidates, dictionary, tfidf):
    scores = {}
    frequencies = FreqDist(candidates)
    for word in set(candidates):
        tf = float(frequencies[word]) / len(frequencies)
        my_id = dictionary.token2id.get(word)
        # accounting for cases where the word
        # has not been seen in the global corpus
        # used to build tfidf model
        if my_id:
            idf = tfidf.idfs[my_id]
        else:
            idf = 0
        scores[word] = tf*idf

    return sorted(scores.iteritems(), key=operator.itemgetter(1), reverse = True)


class CandidateScorer(object):

    def __init__(self, texts):
        self.__texts = texts
        self.__dictionary = corpora.Dictionary(texts)
        self.__tfidf = get_tfidf(texts, self.__dictionary)

    def run(self,candidates):
        return score_candidates(candidates, self.__dictionary, self.__tfidf)


