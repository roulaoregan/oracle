'''
 copyright 2014
 author: Spiridoula O'Regan
 email: roula.oregan@gmail.com
 github user: roulaoregan
'''


class Classifier(object):
	'''
	Super Abstract Classifier has the classify  method
	all subclasses must instantiate this method variable
	'''
	def __init__(self, input_text, languages=['english', 'french','german']):
		self.input_text = input_text
		self.language_ratios = {}
		self.languages = languages
		self.best_match = None


	def classify(self, input):
		pass
