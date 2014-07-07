import os
import re
import sys
import unicodedata
import yaml

import nltk
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.corpus import europarl_raw, genesis, gutenberg, names, stopwords, words
from nltk.corpus import PlaintextCorpusReader


from utilities.training import TrainingData
# freqDist of training intersection for each language with the freqDist of input text, get closest match
#
def OracleClassifier(object):
	def __init__(self, root_dir, document):
		self.en_training_set = None
		self.fr_training_set = None
		self.de_training_set = None
		self.trainer = TrainingData(languages=['english','french','german'], nltk_dir= self.root_dir)
		self.trainer.build_training_set()
		self.root_dir = root_dir
		self.document = document
		self.classifier = {'english':None, 'french': None, 'german': None}
		self.master_word_list = []
		self.word_features = []
	
	# >> REFERENCE:
	#      http://www.nltk.org/book/ch06.html
	#      blog: http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
	###    Test this on the command line!!
	def extract_features(self, document):
		document_words = set(document)
		features = {}
		for word in master_features:
			features['contains(%s)'%word] = word

		return features

	def word_features(self, wordlist):
		wordlist = nltk.FreqDist(wordlist)
		return wordlist.keys()
	
	
	def _assemble(self):
		for (language, wordlist) in self.trainer.data.iteritems():
			self.master_word_list.append((wordlist, language))
		
	def get_words(self):
		all_words = []
		for (words, language) in self.master_word_list:
			all_words.extend(words)
		return all_words
	
	def get_word_features(self, wordlist):
		wordlist = nltk.FreqDist(wordlist)
		return wordlist.keys()

	def train(self):
		self.master_word_list = self._assemble()
		self.word_features = self.get_word_features(self.get_words())

		self.training_set = classify.apply_features(self.extract_features, self.word_features)
		#classifier = nltk.NaiveBayesClassifier.train(training_set)

		self.classifier = NaiveBayesClassifier.train(self.training_set )
		
	def naive_bayes_classifier(self, input_text):
		#print classifier.classify(extract_features(tweet.split()))
		return classifier.classify(self.extract_features(input_text.split()))




def main():
	root_dir = "/Users/spiridoulaoregan/nltk_data"

if __name__ == "__main__":
	sys.exit(main())
