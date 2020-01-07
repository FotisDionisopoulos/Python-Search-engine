#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import string
import math
import os
import re
import sys
import json
import time
import argparse
import operator
from collections import OrderedDict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups



cwd = os.getcwd()
def jaccard_similarity(str1, str2):
	    str1 = set(str1.split(" "))
	    str2 = set(str2.split(" "))
	    return float(len(str1 & str2)) / len(str1 | str2)


def classifying(docs_new):
	tokenize = lambda doc: doc.lower().split(" ")
	categories = ['comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x','misc.forsale','sci.crypt','sci.space', 'alt.atheism', 'soc.religion.christian','comp.graphics','sci.med','rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey','sci.electronics','talk.politics.misc' ,'talk.politics.guns','misc.forsale','talk.politics.mideast','talk.religion.misc']

	twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
	
	metr_dic = {} 

	 
	#in Scikit-Learn

	 
	sklearn_tfidf = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)
	sklearn_representation = sklearn_tfidf.fit_transform(twenty_train)

	for i in range(0,11313):
		jcrd = jaccard_similarity(docs_new, twenty_train.data[i])
		metr_dic[i] = jcrd
	

	doc_ids = dict(sorted(metr_dic.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	doc_ids = OrderedDict(sorted(doc_ids.items(), key=lambda doc_ids: doc_ids[1], reverse=True))
	
	str_re = ''
	for doc_id, sim in doc_ids.iteritems():
		str1 = "Category: " + (twenty_train.target_names[twenty_train.target[doc_id]])
		str2 =  " Jaccard similarity: " + str(sim )
		str_re = ''.join(str_re + str1 + str2 + "\n")
		
	str_re = ''.join(str_re + "***********************" + "\n")
	
	
	return str_re




if (__name__ == "__main__") :

	# -------------------------------------------------------------------------------
	# Text File Parsing
	# -----------------
	with open("classification Jaccard", "w") as f:
		for file in os.listdir(cwd + "/articles"):
		
			if (file.endswith(".txt")):
				completeName = os.path.join(cwd , "articles/"+file) 
				with open(completeName, "r") as fh:
					array1 = []
					for line in fh:
						line  = (line.decode('unicode_escape').encode('ascii','ignore'))
				       		array1.append(line)
				
					array1 = [ ''.join(array1)]
					print "classification",file,"\n"
				
					cl = classifying(array1[0])
					print cl
				
					f.write("Classifying: " +  file +" \n"+ cl+" \n")














