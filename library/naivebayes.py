import operator
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
class OracleClassifier(object):
 	"""docstring for OracleClassifier"""
	def __init__(self, root_dir, input_text=""):
		self.root_dir = root_dir
		self.trainer = TrainingData(languages=['english','french','german'], root_dir= self.root_dir)
		self.trainer.build_training_set()
		self.input_text = input_text
		self.classifier = None
		self.master_word_list = []
		self.word_features = []
	
	# >> REFERENCE:
	#      http://www.nltk.org/book/ch06.html
	#      blog: http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
	###    
	def extract_features(self, input_text):
		document_words = set(input_text)
		features = {}
		for word in self.word_features:
			features['contains(%s)'%word] = (word in document_words)

		return features

	def word_features(self, wordlist):
		wordlist = nltk.FreqDist(wordlist)
		return wordlist.keys()
	
	
	def _assemble(self):
		print "inside assemble"
		all_words = []
		for (language, values) in self.trainer.data.iteritems():
			print language
			print len(values['wordlist'])
			all_words.append((values['wordlist'], language))
		return all_words
		
	def get_words(self):
		all_words = []
		for (words, language) in self.master_word_list:
			all_words.extend(words)
		return all_words
	
	def get_word_features(self, wordlist):
		print "inside get_word_features()"
		wordlist = nltk.FreqDist(wordlist)
		return wordlist.keys()

	def train(self):
		print "inside train"
		self.master_word_list = self._assemble()
		#word_features = get_word_features(
         #           get_words_in_tweets(tweets))
		word_features = self.get_word_features(self.get_words())
		self.word_features = [re.sub(r"([^\w\.\'\-\/,&])", r'', feature) for feature in word_features]
		self.training_set = classify.apply_features(self.extract_features, self.master_word_list)

		print self.training_set
		#training_set = nltk.classify.apply_features(extract_features, tweets)
		#test_set = nltk.classify.apply_features(extract_features, test_tweets)
    	#classifier = nltk.NaiveBayesClassifier.train(training_set)

		self.classifier = NaiveBayesClassifier.train(self.training_set)
		
	def naive_bayes_classifier(self, input_text):

		text = input_text if input_text else self.input_text
		return self.classifier.classify(self.extract_features(text.split()))


def main():
	root_dir = "/Users/spiridoulaoregan/nltk_data"
	genesis_text = "The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy My brothers. And you will know I am the Lord when I lay My vengeance upon you."
	oc = OracleClassifier(root_dir,genesis_text)
	oc.train()
	oc.naive_bayes_classifier(genesis_text)

if __name__ == "__main__":
	sys.exit(main())
