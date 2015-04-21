import operator
import os
import re
import sys
import unicodedata
import yaml

from library.classifier import Classifier
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

# Simple classifier that uses NLTK stopwords to identify language
# reference: blog: http://blog.alejandronolla.com/2013/05/15/detecting-text-language-with-python-and-nltk/

class SimpleSimon(Classifier):
	def __init__(self, input_text):
		Classifier.__init__(self, input_text)

	def classify(self):
		tokens = wordpunct_tokenize(self.input_text)
		input_words = [word.lower() for word in tokens]

		for language in self.languages:
			stopwords_set = set(stopwords.words(language))
			input_words_set = set(input_words)

			common_words = stopwords_set.intersection(input_words_set)
			self.language_ratios[language] = len(common_words)

			self.best_match = sorted(self.language_ratios.iteritems(), key=operator.itemgetter(1), reverse=True)

			return self.best_match[0]



