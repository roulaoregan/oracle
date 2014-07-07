import os
import re
import sys
import unicodedata
import yaml

import nltk
import nltk.classify
from nltk.corpus import europarl_raw, genesis, gutenberg, names, stopwords, words
from nltk.corpus import PlaintextCorpusReader

from utilities.training import TrainingData

def OracleClassifier(object):
	def __init__(self, root_dir, document):
		self.en_training_set = None
		self.fr_training_set = None
		self.de_training_set = None
		self.root_dir = root_dir
		self.document = document
	#http://www.nltk.org/book/ch06.html
	#blog
	### Test this on the command line!!
	def extract_features(document):

		features = {}
		for word in 
		return features

	def build_training_set(self):
		training_set = TrainingData(languages=['english','french','german'], nltk_dir= self.root_dir)
		training_set.build_training_set()


	def train(self, document, master_features):
		document_words = set(document)
		features = {}
		for word in master_features:
			features['contains(%s)'%word] = word

		return features


	def naive_bayes_classifier(self):
		pass




def main():
	root_dir = "/Users/spiridoulaoregan/nltk_data"

if __name__ == "__main__":
	sys.exit(main())
