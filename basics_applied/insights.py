__author__ = 'a_medelyan'

# Goal: putting together categorized documents and keyword extraction
# How do we find out, what makes a good movie?

from nltk.corpus import movie_reviews
from nltk.probability import  FreqDist
from basics_applied import keyword_extractor

candidate_extractor = keyword_extractor.CandidateExtractor()

texts = []
texts_ids = {}

# Step 1. Apply candidate extraction on each review

candidate_scorer = keyword_extractor.CandidateScorer(texts)


# Step 2. For review in each category extract most common 20 keywords
# Then display the most common 50 keywords per category


