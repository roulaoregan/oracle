'''
 copyright 2014
 author: Spiridoula O'Regan
 email: roula.oregan@gmail.com
 github user: roulaoregan
'''
#!/usr/bin/python
import argparse
import re
import os
import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

from library.naivebayes import OracleClassifier
from library.simple import SimpleSimon
from library.ngram_classifier import NgramClassifier

'''
Simple command line tool that attempts to determine whether the input text language is in 
either English, French or German.

@todo: 
* move training data set to preprocess
* improve Supervised learning with threading
* implement Sleeper Algorithms
* implement Unsupervised Unstructured Learning
'''

def read_file(file_path):
	text = None
	if file_path:
		if os.path.exists(file_path):
			with open(file_path) as fp:
				text = fp.read()
	
	return text


def main(argv):
	cprint(figlet_format('Oracle', font='bubble'),
       'green', attrs=['bold'])
	parser = argparse.ArgumentParser(description="Oracle Language Classifier")
	parser.add_argument('-f', '--file', 
			    help=' /path/to/file/text_file.txt', 
			    required=False)
	parser.add_argument('-i', '--input', 
			    help='This is input text to be analyzed by Oracle', 
			    required=False)
	parser.add_argument('-b', '--naivebayes', 
	  		    action='store_true', 
			    help="Statistical classifier", 
			    required=False)
	parser.add_argument('-s', '--simple', 
			    action='store_true', 
			    help="Simple classifier", 
			    required=False)
	parser.add_argument('-v', '--verbose', 
	                    help="increase output verbosity", 
	                    required=False)
	parser.add_argument('-n', '--ngram', 
			    action='store_true', 
			    help='N-gram classifier', 
			    required=False)
	parser.add_argument('-e', '--sleeper', 
			    action='store_true', 
			    help='Sleeper expert classifier', 
			    required=False)
	parser.add_argument('-u', '--unstructured', 
			    action='store_true', 
	                    help='Unstructured Text classifier', 
	                    required=False)
	parser.add_argument('-c', '--corpus', 
			    help='File path to corpus', 
			    required=False)

	args = parser.parse_args()

	if args.input is None and args.file is None:
		print IOError("No input text or file path provided! "
			      "\n>>>>> Please enter input text as: \"This is a string\"")
		
		return

	text = args.input if args.input else read_file(args.file)
	if not text:
		print IOError("File does not exist")
		return

	if args.simple:
		classifer = SimpleSimon(text)
	elif args.naivebayes:
		if not args.corpus:
			print IOError("No corpus file path provided!"
				      "\n>>>>naivebayes requires training corpus")
			return
		classifer = OracleClassifier(args.corpus, text)
		
	elif args.ngram:
		classifer = NgramClassifier(text)
	else:
		print(">>>> No classifer choosen - using default classifier: SimpleSimon")
		classifer = SimpleSimon(text)

	print "#---------------------------------------------------#"	
	print "# %s classification for input text:"%classifer.__class__.__name__
	print "#---------------------------------------------------#"

	print">>>>", classifer.classify()[0].title(), "<<<<<"
	return


if __name__ == "__main__":
   main(sys.argv[1:])
