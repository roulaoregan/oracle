# coding=utf-8
import operator
import os
import re
import sys
import unicodedata
import json
import yaml
import nltk



def load_yaml_configs(filepath):
	data = {}
	if os.path.exists(filepath):
		with open(filepath, 'r') as y:
			data.update(yaml.safe_load(y))
	return data


def load_json_file(filepath):
	data = {}
	if os.path.exists(filepath):
		print "filepath: %s"%filepath
		with open(filepath, "r") as js:
			data = json.load(js)
	return data
