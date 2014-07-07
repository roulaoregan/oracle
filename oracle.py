import os
import re
import sys


from optparse import OptionParser



##################
# Driver
##################
def main():
	arg_handler = OptionParser("****************  Oracle Language Predictor  ****************")
	arg_handler.add_option('-f', '--file', type='string', \
		help=' /path/to/file/text_file.txt')
	arg_handler.add_option("-i", "--input", type="string", \
		help="\"This is input text to be analyzed by Oracle\"")
	arg_handler.add_option('-nbc', '--naivebayesclassifier')
	arg_handler.add_option('-s', '--simpleset')
	arg_handler.add_option('-n', '--ngram')
	options, args = arg_handler.parse_args()
	option_dict = vars(options)

	file_name = None
	if arg_handler.get_option("-f"):
		file_name = option_dict['file']
		if not os.path.exists(file_name):
			raise FileInputError("file path does NOT exist!")

	if arg_handler.get_option("-i"):
		text = option_dict['input']
		if not text:
			raise FileInputError("No input text provided! Please enter input text as: \"This is a string\"")



if __name__ == "__main__":
	sys.exit(main())
