#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import time
import argparse

from sklearn.metrics import jaccard_similarity_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity  
from sklearn.metrics.pairwise import linear_kernel
cwd = os.getcwd()

def classifying(docs_new):
	#poies katigories tha xrisimopoiisoume
	categories = ['comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x','misc.forsale','sci.crypt','sci.space', 'alt.atheism', 'soc.religion.christian','comp.graphics','sci.med','rec.autos','rec.motorcycles','rec.sport.baseball','rec.sport.hockey','sci.electronics','talk.politics.misc' ,'talk.politics.guns','misc.forsale','talk.politics.mideast','talk.religion.misc']
	#fortosi arxeiwn pou antistoixoun stis epilegmenes katigories	
	twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)



	#dimiourgia dianysmatos xaraktirwn
	count_vect = CountVectorizer()
	X_train_counts = count_vect.fit_transform(twenty_train.data)
	X_train_counts.shape
	count_vect.vocabulary_.get(u'algorithm')
	#ypologismos tf-idf
	tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)

	#eyresi xaraktisristikon 
	X_train_tf = tf_transformer.transform(X_train_counts)
	X_train_tf.shape
	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	X_train_tfidf.shape


	#eyresi xaraktisristikon kai tf-idf gia to diko mas arxeio
	X_new_counts = count_vect.transform(docs_new)
	X_new_tfidf = tfidf_transformer.transform(X_new_counts)
	

	cosine_similarities = linear_kernel(X_new_tfidf, X_train_tfidf).flatten()
	related_docs_indices = cosine_similarities.argsort()[:-5:-1]
	str_re = ''

	
	for i in related_docs_indices:
		str1 = "Category: " + (twenty_train.target_names[twenty_train.target[i]])
		str2 =  " Cosine similarity: " + str(cosine_similarities[i] )
		str_re = ''.join(str_re + str1 + str2 + "\n")
		
	str_re = ''.join(str_re + "***********************" + "\n")
	
	
	return str_re


if (__name__ == "__main__") :

	# -------------------------------------------------------------------------------
	# Text File Parsing
	# -----------------
	with open("classification Cosine", "w") as f:
		for file in os.listdir(cwd + "/articles"):
		
			if (file.endswith(".txt")):
				completeName = os.path.join(cwd , "articles/"+file) 
				with open(completeName, "r") as fh:
					array1 = []
					for line in fh:
						line  = (line.decode('unicode_escape').encode('ascii','ignore'))
				       		array1.append(line)
				
					array1 = [ ''.join(array1)]
					print "classification",file
					cl = classifying(array1)
					print cl
				
					f.write("Classifying: " +  file +" \n"+ cl+" \n")
















	
