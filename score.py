from sklearn.feature_extraction.text import TfidfVectorizer
import sys
import json
import numpy as np

selection = sys.argv[0]
json_body = sys.argv[1]
items     = json.load(json_body)['items']
text      = [item['caption']['text'] for item in items]
items.insert(text, selection)

vect = TfidfVectorizer(stop_words='english')
tfidf = vect.fit_transform(text)

scores = (tfidf * tfidf.T).A[1:, 0]
sorted_scores_desc = sorted(scores, reverse=True)

print ', '.join(map(str, sorted_scores_desc))
