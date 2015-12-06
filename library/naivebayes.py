'''
 copyright 2014
 author: Spiridoula O'Regan
 email: roula.oregan@gmail.com
 github user: roulaoregan
'''
# coding=utf-8
import nltk
import operator
import os
import re
import sys
import unicodedata

from classifier import Classifier
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.probability import ELEProbDist, FreqDist
from nltk.corpus import europarl_raw, genesis, gutenberg, names, stopwords, words
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from utilities.training import TrainingData, get_corpus
from utilities import utils

'''
freqDist of training intersection for each language with the freqDist of input text, get closest match
todo: 
- add probability to classifier
- add logger 

''' 
class OracleClassifier(Classifier):
 	"""OracleClassifier:  language identification classifier using NaiveBayes
 						  inherits from Classifier super class

 	"""
	def __init__(self, root_dir, input_text, config_dirs):
		Classifier.__init__(self, input_text)

		self.master_word_list = []
		self.word_features = []
		self.configs = utils.load_json_file(config_dirs)

	def get_words_in(self, words):
		all_words = []
		for (word, language) in words:
			all_words.append(word)
		return all_words

	def word_feats(self, wordlist):
		wordlist = nltk.FreqDist(wordlist)
		word_features = wordlist.keys()
		return word_features


	def extract(self, document):
		features = {}
		for word in self.word_features:
			features['contains(%s)' % word] = (word in document)

		return features

		
	def classify(self, input_text=None):

		training_text = []

		for language in self.languages:

			corpusdir = os.path.join(self.configs['dirs']['CORPUS_DIR'], language)
			stopwrds = stopwords.words(language)
			training_text.extend([(w.lower(), language) for w in get_corpus(corpusdir) if len(w) >= 2 and w not in stopwrds])

		self.word_features = self.word_feats(self.get_words_in(training_text))

		training_set = nltk.classify.apply_features(self.extract, training_text)
		classifier = nltk.NaiveBayesClassifier.train(training_set)

		classifier = nltk.NaiveBayesClassifier.train(training_set)

		text = input_text if input_text else self.input_text
		prediction = classifier.classify(self.extract(self.input_text))
		
		return prediction

'''
test
'''
def main():
	snow_queen = get_corpus(corpusdir="/Users/spiridoulaoregan/nltk_data/test_data", filename="snow_queen_german.txt")
	#root_dir, input_text, config_dirs
	oc = OracleClassifier(root_dir="/home/roulaoregan/algo/nltk_data", input_text=snow_queen, config_dirs=os.path.join(os.getcwd(), "configs", "dirs.json"))
	print  "classified: ", oc.classify()


if __name__ == "__main__":
	sys.exit(main())
