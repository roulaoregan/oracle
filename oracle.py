#!/usr/bin/python
import os
import re
import sys
import argparse

from library.naivebayes import OracleClassifier
from library.simple import SimpleSimon
from library.ngram_classifier import NgramClassifier


def read_file(file_path):
	text = None
	if file_path:
		if os.path.exists(file_path):
			with open(file_path) as fp:
				text = fp.read()
	
	return text


def main(argv):
	#parser = argparse.ArgumentParser(description='Description of your program')
	#parser.add_argument('-f','--foo', help='Description for foo argument', required=False)
	#parser.add_argument('-b','--bar', help='Description for bar argument', required=False)
	parser = argparse.ArgumentParser(description=">>>>>>>>> ORACLE Language Predictor <<<<<<<<<<<")
	parser.add_argument('-f', '--file', help=' /path/to/file/text_file.txt', required=False) #, required=True)
	parser.add_argument('-i', '--input', help='This is input text to be analyzed by Oracle', required=False) #, required=True)
	parser.add_argument('-b', '--naivebayes', help="Statistical classifier", required=False)
	parser.add_argument('-s', '--simple', action='store_true', help="Simple classifier", required=False)
	parser.add_argument('-v', '--verbose', help="increase output verbosity", required=False)
	parser.add_argument('-n', '--ngram', help='N-gram classifier', required=False)
	parser.add_argument('-e', '--sleeper', help='Sleeper expert classifier', required=False)
	parser.add_argument('-u', '--unstructured', help='Unstructured Text classifier', required=False)
	parser.add_argument('-c', '--corpus', help='File path to corpus', required=False)

	#args = vars(parser.parse_args())
	args = parser.parse_args()

	if args.input is None and args.file is None:
		print IOError("No input text or file path provided! \n>>>>> Please enter input text as: \"This is a string\"")
		#print(IOError("No input to analyze: please provide input string or file path"))
		return

	text = args.input if args.input else read_file(args.file)
	if not text:
		print IOError("File does not exist")
		return

	if args.simple:
		classifer = SimpleSimon(text)
	elif args.naivebayes:
		if not args.corpus:
			print IOError("No corpus file path provided! \n>>>>naivebayes requires training corpus")
			return
		classifer = OracleClassifier(args.corpus, text)
		classifier.train()
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
