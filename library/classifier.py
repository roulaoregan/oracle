#Super Abstract Classifier has the classify  method
#all subclasses must instantiate this method variable
#
#

class Classifier(object):
	def __init__(self, input_text, languages=['english', 'french','german']):
		self.input = input_text
		self.languages = languages

	def classify(self, input):
		pass
