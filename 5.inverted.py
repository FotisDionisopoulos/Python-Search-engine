#!/usr/bin/env python
from __future__ import division, unicode_literals
import math
import os
import time
import sys
from textblob import TextBlob as tb
import unicodedata

cwd = os.getcwd()

def tfidf(word, blob, bloblist):
	tf = blob.words.count(word) / len(blob.words)
	n_containing = sum(1 for blob in bloblist if word in blob.words)
	idf = math.log(cnt / (1 + n_containing))
   	return tf*idf

def word_split(text):
    """
    Split a text in words. Returns a list of tuple that contains
    (word, location) location is the starting byte position of the word.
    """
    word_list = []
    wcurrent = []


    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
        elif wcurrent:
            word = ''.join(wcurrent)
            word_list.append( word)
            wcurrent = []

    if wcurrent:
        word = ''.join(wcurrent)
        word_list.append( word)

    return word_list



def words_normalize(words):

    normalized_words = []
    for  word in words:
        wnormalized = word.lower()
        normalized_words.append(wnormalized)
    return normalized_words

def word_index(text):

    words = word_split(text)
    words = words_normalize(words)
    return words


def inverted_index(text, doc_id):
    for  word in word_index(text):
	tf_idf = tfidf(word, documents[doc_id], bloblist)
	
	if tf_idf !=0 :
				
			if word in inverted.keys() :
				if doc_id not in inverted[word]:
					inverted.setdefault(word,[]).append(doc_id)
					inverted.setdefault(word,[]).append(tf_idf)
			else:
				inverted.setdefault(word,[]).append(doc_id)
				inverted.setdefault(word,[]).append(tf_idf)
	

    return inverted

cnt = 0
inverted = {}
indices = {}
bloblist = []
documents = {}
if __name__ == '__main__':


    # Build Dictionaries
    for file in os.listdir(cwd+ "/articles/"):
		
		if (file.endswith(".txt")):
			cnt+=1
			print file
			
			completeName = os.path.join(cwd , "articles/"+file)
			print completeName
			with open(completeName, "r") as fh:
				array1 = []
				for line in fh:
					line  = (line.decode('unicode_escape').encode('ascii','ignore'))
				       	array1.append(line)
				array1 = [ ''.join(array1)]
				
				for value in array1:
					value = str(value)
					documents[file] = tb(value)
					bloblist.append(tb(value))


    # Build Inverted-Index for documents
    for file in os.listdir(cwd + "/articles"):
		
		if (file.endswith(".txt")):
			cnt+=1
			print file
			completeName = os.path.join(cwd , "articles/"+file)
			with open(completeName, "r") as fh:
				array1 = []
				for line in fh:
					line  = (line.decode('unicode_escape').encode('ascii','ignore'))
				       	array1.append(line)
				array1 = [ ''.join(array1)]				
				
				for doc_id, text in documents.iteritems():
					for value in array1:
        					doc_index = inverted_index(value, doc_id)
        				

    with open("inverted_index.xml", "w") as fh:
	    fh.write( "<inverted_index>"+"\n")
	    for word, values in inverted.iteritems():
		fh.write("<lemma name=\""+word+"\">"+"\n")
		i = 1
		flag = 0
		for value in values:
			if i == 1 :
				fh.write("<document id=\"%s\"" % value)
				indices[word] = value
				i+=1
			elif i == 2 :
				fh.write( " weight=\"%f\"/>" %value+"\n")
				i=1

		fh.write("</lemma>"+"\n")
	    fh.write("</inverted_index>")








    
