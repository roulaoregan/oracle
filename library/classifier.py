#Super Abstract Classifier has the classify  method
#all subclasses must instantiate this method variable
#
#

class Classifier(object):
	def __init__(self, input_text, languages=['english', 'french','german']):
		self.input_text = input_text
		self.language_ratios = {}
		self.languages = languages
		self.best_match = None


	def classify(self, input):
		pass
