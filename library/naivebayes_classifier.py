import os
import re
import sys
import unicodedata
import yaml

import nltk
from nltk import classify
from nltk.corpus import europarl_raw, genesis, gutenberg, names, stopwords, words
from nltk.corpus import PlaintextCorpusReader

from utilities.training import TrainingData

def OracleClassifier(object):
	def __init__(self, root_dir, document):
		self.en_training_set = None
		self.fr_training_set = None
		self.de_training_set = None
		self.trainer = TrainingData(languages=['english','french','german'], nltk_dir= self.root_dir)
		self.trainer.build_training_set()
		self.root_dir = root_dir
		self.document = document
	
	
	# >> REFERENCE:
	#      http://www.nltk.org/book/ch06.html
	#      blog: http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
	###    Test this on the command line!!
	def extract_features(self, document, master_features):
		document_words = set(document)
		features = {}
		for word in master_features:
			features['contains(%s)'%word] = word

		return features

	def word_features(self, wordlist):
		wordlist = nltk.FreqDist(wordlist)
		return wordlist.keys()
	
	def train(self):
		self.en_training_set = classify.apply_features(self.extract_features, \
								self.trainer.data['english']['wordlist'])
		self.fr_training_set = classify.apply_features(self.extract_features, \
								self.trainer.data['french']['wordlist'])
		self.de_training_set = classify.apply_features(self.extract_features, \ 
								self.trainer.data['german']['wordlist'])
	def naive_bayes_classifier(self):
		pass




def main():
	root_dir = "/Users/spiridoulaoregan/nltk_data"

if __name__ == "__main__":
	sys.exit(main())
