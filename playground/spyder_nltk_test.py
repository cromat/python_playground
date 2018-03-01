# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
from nltk.book import *
from nltk.collocations import *
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))

filtered_tokens = []
for token in text1.tokens:
    if token.lower() not in stop and token.isalpha():
        filtered_tokens.append(token.lower())

#print(filtered_tokens)

finder = BigramCollocationFinder.from_words(filtered_tokens)
finder.apply_freq_filter(4)

ngram = list(finder.ngram_fd.items())
ngram.sort(key=lambda item: item[-1], reverse=True)

print(ngram)