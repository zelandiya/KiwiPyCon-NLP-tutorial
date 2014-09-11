__author__ = 'a_medelyan'

from nltk.corpus import movie_reviews
import keyword_extractor


candidate_extractor = keyword_extractor.CandidateExtractor()

texts = []
count = 0
for fileid in movie_reviews.fileids():
    words = candidate_extractor.run(movie_reviews.words(fileid))
    texts.append(words)
    count += 1
    if count % 100 == 0:
        print 'Added ', count, ' files'

candidate_scorer = keyword_extractor.CandidateScorer(texts)

words = movie_reviews.words('neg/cv977_4776.txt')

candidates = candidate_extractor.run(words)

print candidate_scorer.run(candidates)