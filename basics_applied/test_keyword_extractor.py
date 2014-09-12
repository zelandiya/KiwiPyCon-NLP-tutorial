__author__ = 'a_medelyan'

from nltk.corpus import movie_reviews
import keyword_extractor


candidate_extractor = keyword_extractor.CandidateExtractor()

# First create the texts object to create the tfidf model
# in the CandidateScorer constructor

texts = []
count = 0
for fileid in movie_reviews.fileids():
    words = candidate_extractor.run(movie_reviews.words(fileid))
    texts.append(words)
    count += 1
    if count % 100 == 0:
        print 'Added ', count, ' files'

candidate_scorer = keyword_extractor.CandidateScorer(texts)

# Then extract keywords from a given review
words = movie_reviews.words('pos/cv994_12270.txt')

# 1. Extract candidates
candidates = candidate_extractor.run(words)

# 2. Rank candidates by TFxIDF
print candidate_scorer.run(candidates)