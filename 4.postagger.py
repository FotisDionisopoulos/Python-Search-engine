#!/usr/bin/env python
from nltk import word_tokenize, pos_tag	
import os
import sys
cwd = os.getcwd()



if __name__ == '__main__':
    if not os.path.exists(cwd + "/PosTagger"):
    	os.makedirs(cwd + "/PosTagger")
     
   
    # Build Dictionaries
    for file in os.listdir(cwd + "/articles/"):
		
		if (file.endswith(".txt")):
			print file
			completeName = os.path.join(cwd , "articles/"+file)
			with open(completeName, "r") as fh:
				array = []
				for line in fh:
					
					tag = pos_tag(line.split())
					array.append(str(tag))
			completeName = os.path.join(cwd , "PosTagger/"+file)
			print completeName
			with open( completeName, "w") as fhs:
				for val in array:
					print val
					fhs.write(val + "\n" )
