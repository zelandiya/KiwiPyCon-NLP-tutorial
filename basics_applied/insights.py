__author__ = 'a_medelyan'
from nltk.corpus import movie_reviews
from nltk.probability import  FreqDist
from basics_applied import keyword_extractor

# Goal: putting together categorized documents and keyword extraction
# How do we find out, what makes a good movie?


candidate_extractor = keyword_extractor.CandidateExtractor()

texts = []
count = 0
texts_ids = {}
for fileid in movie_reviews.fileids():
    words = candidate_extractor.run(movie_reviews.words(fileid))
    texts.append(words)
    # Here, we memorize which list element in texts
    # contains the candidates for that fileid
    texts_ids[fileid] = count
    count += 1
    if count % 100 == 0:
        print 'Added ', count, ' files'

candidate_scorer = keyword_extractor.CandidateScorer(texts)

for category in movie_reviews.categories():

    print 'Category', category
    all_keywords = []
    for fileid in movie_reviews.fileids(categories=category):

        # Retrieve the candidates from the previously
        # computed list
        count = texts_ids[fileid]
        candidates = texts[count]

        # Extract keywords
        keywords = candidate_scorer.run(candidates)[:20]

        # Add keywords to the global list
        for keyword in keywords:
            all_keywords.append(keyword[0])

            # Add n-grams twice to boost their score
            if ' ' in keyword[0]:
                all_keywords.append(keyword[0])

    all_words_by_frequency = FreqDist(all_keywords)
    print all_words_by_frequency.items()[:50]
