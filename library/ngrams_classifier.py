'''
 copyright 2014
 author: Spiridoula O'Regan
 email: roula.oregan@gmail.com
 github user: roulaoregan
'''
import operator
import os
import re
import sys
import unicodedata
import yaml
import nltk

from library.classifier import Classifier
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
from utilities.training import TrainingData


# Referenced Tutorial:  http://blog.alejandronolla.com/2013/05/20/n-gram-based-text-categorization-categorizing-text-with-python/
#						https://github.com/z0mbiehunt3r/ngrambased-textcategorizer/blob/master/ngramfreq.py 

class NgramClassifier(Classifier):
	def __init__(self, root_dir, input_text, n=4):
		Classifier.__init__(self, input_text)
		self.root_dir = root_dir
		self.language_ratios = {}
		self.n = n
		self.languages = languages
		self.tokenizer = RegexpTokenizer("[a-zA-Z'`]+")
		self.train = TrainingData(languages=self.languages, 
								  config_dir="/Users/spiridoulaoregan/Documents/oracle/python/library/configs", 
								  root_dir=root_dir)
		self._train_data()
		self.input_text = ""
		self.frequencies = dict(zip([lang for lang in languages], 
									[{} for x in languages]))
		self._analyze_data()
		

	def _train_data(self):
		self.train.build_training_set()
		self.training_data = self.train.data

	def _analyze_data(self):

		for language in self.frequencies:
			wordlist = self.train.data[language]['wordlist']

			generated_ngrams = ngrams(" ".join(wordlist), self.n, pad_left=True, pad_right=True, pad_symbol=' ')

			ngrams_list = ["".join(e.lower() for e in tpl).strip() for tpl in generated_ngrams]
			for ngram in ngrams_list:
				try:
					self.frequencies[language][ngram]+= 1
				except KeyError:
					self.frequencies[language][ngram] = 1


	def predict_language(self):
		""" Will try guessing text's language by computing Ngrams and comparing
        them against the training data. 
        Find Minimum`Distance" takes the distance measures from all of the 
        category profiles to the document profile, and picks the smallest one.
        """

		tokens = self.tokenizer.tokenize(self.input_text)
		generated_ngrams = ngrams(" ".join(["".join(e.lower() for e in tpl).strip() for tpl in tokens]), \
															4, pad_left=True, pad_right=True, pad_symbol=' ')

		#ngram_stats_sorted = sorted(ngram_stats.iteritems(), key=operator.itemgetter(1), reverse=True)
		
		# compare profiles with input text and each language stat
		for language in self.languages:
			distance = self.compare_ngram_distances(generated_ngrams,self.frequencies[language])
			self.language_ratios[language] = distance

		best_match = sorted(self.language_ratios.iteritems(), key=operator.itemgetter(1))
		return best_match

	def compare_ngram_distances(self, input_profile, training_profile):
		'''
		Measure how far out of place an N-gram in one profile is from its
		place in the other profile.
		'''
		document_distance = 0
		category_ngrams = [ngram[0] for ngram in training_profile] 
		document_ngrams = [ngram[0] for ngram in input_profile]
		
		max_out_order = len(document_ngrams)
		
		category_profile_index = None
		for ngram in document_ngrams:
			document_index = document_ngrams.index(ngram)
			try:
				category_profile_index = category_ngrams.index(ngram)

			except ValueError:
				category_profile_index = max_out_order

			distance = abs( (category_profile_index - document_index) )
			document_distance += distance

		return document_distance
	
	def classify(self):
		pass



def main():
	root_dir = "/Users/spiridoulaoregan/nltk_data"
	genesis_text = "The path of the righteous man is beset on all sides by the inequities of the \
					selfish and the tyranny of evil men. Blessed is he who, in the name of charity \
					and good will, shepherds the weak through the valley of the darkness, for he is \
					truly his brother's keeper and the finder of lost children. And I will strike \
					down upon thee with great vengeance and furious anger those who attempt to poison \
					and destroy My brothers. And you will know I am the Lord when I lay My vengeance upon you."
	classifier = NgramClassifier(root_dir, languages=['english', 'french','german'])
	print classifier.predict_language(genesis_text)

if __name__ == "__main__":
	sys.exit(main())
