import operator
import os
import re
import sys
import unicodedata
import yaml

from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams
#http://blog.alejandronolla.com/2013/05/20/n-gram-based-text-categorization-categorizing-text-with-python/
from utilities.training import TrainingData

tokenizer = RegexpTokenizer("[a-zA-Z'`éèî]+")
word_list = tokenizer.tokenize("Le temps est un grand maître, dit-on, le malheur est qu'il tue ses élèves.")

input_text = " ".join(word_list)
generated_ngrams = ngrams(input_text, 4, pad_left=True, pad_right=True, pad_symbol=' ')

ngram_test3 = ["".join(e.lower() for e in tpl).strip() for tpl in generated_ngrams]

ngram_stats = {}
for ngram in ngram_test3:
	try:
		ngram_stats[ngram]+= 1
	except KeyError:
		ngram_stats[ngram] = 1

ngram_stats_sorted = sorted(ngram_stats.iteritems(), key=operator.itemgetter(1), reverse=True)

# Pre computed training data
#

class NgramClassifier(object):
	def __init__(self, languages=[]):
		self.tokenizer = RegexpTokenizer("[a-zA-Z'`éèî]+")
		self.train = TrainingData(languages=['english','french','german'], \
									nltk_dir="/Users/spiridoulaoregan/nltk_data")
		self.training_data = {}
		self.training_stats = {}
		self.input_text = ""
		self.frequencies = dict(zip([lang for lang in languages], \
													[{'frequencies':[]} for x in languages]))
		self._train_data()
		self._analyze_data()
		

	def _train_data(self):
		self.train.build_training_set()
		self.training_data = self.train.data

	def _analyze_data(self):

		for language in self.frequencies:
			wordlist = self._train_data[language]['wordlist']
			tokens = tokenizer.tokenize(" ".join([w.lower() for w in \
											self._train_data[language]['wordlist']]))

			generated_ngrams = ngrams(" ".join(wordlist), 4, pad_left=True, pad_right=True, pad_symbol=' ')

			ngrams = ["".join(e.lower() for e in tpl).strip() for tpl in generated_ngrams]
			for ngram in ngrams:
				try:
					self.training_stats[ngram]+= 1
				except KeyError:
					self.training_stats[ngram] = 1

	def _count(self, ngrams, dictionary):
			for ngram in ngrams:
				try:
					dictionary[ngram]+= 1
				except KeyError:
					dictionary[ngram] = 1

	def predict_language(self, input_text):
		self.input_text = input_text
		tokens = tokenizer.tokenize(input_text)
		generated_ngrams = ngrams(" ".join(["".join(e.lower() for e in tpl).strip() for tpl in tokens]), \
															4, pad_left=True, pad_right=True, pad_symbol=' ')




def main():
	root_dir = "/Users/spiridoulaoregan/nltk_data"
	genesis_text = "The path of the righteous man is beset on all sides by the inequities of the selfish and the tyranny of evil men. Blessed is he who, in the name of charity and good will, shepherds the weak through the valley of the darkness, for he is truly his brother's keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy My brothers. And you will know I am the Lord when I lay My vengeance upon you."
	oc = OracleClassifier(root_dir,genesis_text)
	oc.train()
	oc.naive_bayes_classifier(genesis_text)

if __name__ == "__main__":
	sys.exit(main())









