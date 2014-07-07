import os
import re
import sys
import unicodedata
import yaml

import nltk
import nltk.classify
from nltk.corpus import europarl_raw, genesis, gutenberg, names, stopwords, words
from nltk.corpus import PlaintextCorpusReader
# make corpus give some txt
#
def euro_parliment(language='english'):
	language_words = europarl_raw.german if language == 'german' else europarl_raw.french if language == 'french' else europarl_raw.english
	de = europarl_raw.german
	#use isinstance(unicode, str) --> check for correct syntax
	words = [ unicodedata.normalize("NKFD", e).encode("ascii", "ignore").lower() \
									for e in de.words() if re.match(r'[aA-zZ]',e)]
	return words

def genesis(text='english.txt'):

	genesis_dir = nltk.data.find('corpora/genesis.zip').join('genesis/')
	my_genesis = nltk.corpus.PlaintextCorpusReader(genesis_dir, '.*\.txt', sent_tokenizer=nltk.RegexpTokenizer('[^.!?]+'))
	genesis_text = my_genesis.words(text)
	return [e.lower() for e in genesis_text if re.match(r"[aA-zZ]",e)]

def get_corpus(corpusdir):
	newcorpus = PlaintextCorpusReader(corpusdir, '.*')
	titles = newcorpus.fileids() # returns all the .txt files in the dir
	words = []
	for title in titles:
		newcorpus_txt = newcorpus.words(title)
		words.extend([ e for e in newcorpus_txt if re.match(r"[aA-zZ]",e)])
	
	return words

class TrainingData(object):
	def __init__(self, languages, root_dir=""):

		self.languages = dict(zip([x for x in languages],[{'wordlist': [], 'word_features':[]} for x in languages]))
		print ">>self.languages: %s"%self.languages
		self.directories = {}
		config_files = os.path.join(os.getcwd(), "configs", "corpora.yaml")
		if os.path.exists(config_files):
			with open(config_files) as f:
				self.directories = yaml.load(f)
		else:
			raise FileInputError("Was not able to find \"config\" directory in directory")
		self.root_dir = root_dir

	@property        
	def data(self):
		return self.languages
		
	def get_features(self, language):
		return self.languages[language]['feature_vector']
	def get_words(self, language):
		return self.languages[language]['wordlist']
	#Handle Exception KeyError 
	def all_words(self, language):
		
		wordlist = []
		corpus_dirs = self.directories[language]

		for corpus_dir in corpus_dirs:
			wordlist.extend(get_corpus(os.path.join(self.root_dir,corpus_dir)))

		return wordlist

	def build_training_set(self):
		#root_dir = self.root_dir if not root_dir else root_dir
		
		for (language, wordlist) in self.languages.iteritems():

			wordlist = self.all_words(language)
			self.languages[language]['wordlist'] = wordlist
			self.languages[language]['feature_vector'] = nltk.FreqDist(wordlist)
			#to get word_features do: self.languages[language]['feature_vector'].keys()		


######################
# Test TraingingData
######################
def main():
	training = TrainingData(languages=['english','french','german'], root_dir="/Users/spiridoulaoregan/nltk_data")
	training.build_training_set()

if __name__ == "__main__":
	sys.exit(main())
	





