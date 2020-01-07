#!/usr/bin/env python
import unicodedata
import os
import re
from nltk import pos_tag
import sys
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

wp_tokenizer = WordPunctTokenizer()			# Tokenizer instance
wnl_lemmatizer = WordNetLemmatizer()		# Wordnet Lemmatizer instance
stop_words = stopwords.words('english')		# English stop words list
cwd = os.getcwd()
ccc = ['CD','CC','DT','EX','IN','LS','MD','PDT','POS','PRP','PRP$','RP','TO','UH','WDT','WP','WP$','WRB']
def rm(text):
	text = ' '.join([word for word in text.split() if word not in stopwords.words("english")])	
	return text

def rm2(text):
	text = ' '.join([word for word, pos in pos_tag(wp_tokenizer.tokenize(text.lower().strip())) if word not in ccc])
	return text


if __name__ == '__main__':

    # Build Dictionaries
    for file in os.listdir(cwd + "/articles"):
		
		if (file.endswith(".txt")):
			print file
			completeName = os.path.join(cwd , "articles/"+file)
			with open(completeName, "r+") as fh:
				array = []
				for line in fh:
					line  = (line.decode('unicode_escape').encode('ascii','ignore'))
					line  = rm( line )
					line  = rm2( line )
					
					array.append(str(line))
			with open(completeName, 'w'): pass	 
			with open(completeName, "r+") as fh:
				for val in array:

					print val
					fh.write(val + "\n" )
					       
				
				
				



