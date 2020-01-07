#!/usr/bin/env python
import xml.etree.ElementTree as ET
import sys
import operator
from collections import OrderedDict

tree = ET.parse('inverted_index.xml')
root = tree.getroot()
inverted = {}
print root.tag
for lemma in root.findall('lemma'):
     lem = lemma.get('name')
     for doc in lemma.findall('document'):
	     docID = doc.get('id')
	     weight = doc.get('weight')
 	     if lem in inverted.keys() :
				if docID not in inverted[lem]:
					inverted.setdefault(lem,[]).append(docID)
					inverted.setdefault(lem,[]).append(weight)
	     else:
				inverted.setdefault(lem,[]).append(docID)
				inverted.setdefault(lem,[]).append(weight)
	     


# Search something and print results
while 1:

	try:
		queries = raw_input("query: ")
	except KeyboardInterrupt:
		sys.exit("\nBye!")

	found = 0

    	sorted_inv = {}
	
	
	for query in queries.split():
		if query in inverted.keys():
			
			
		    	docs_weights = inverted[query]
			for i in range(0,len(docs_weights)-1,2):
				
				if docs_weights[i] in sorted_inv.keys():
					sorted_inv[docs_weights[i]] = float(sorted_inv[docs_weights[i]]) + float(docs_weights[i+1])
				else:
					sorted_inv[docs_weights[i]] = docs_weights[i+1]
				
			
    				
			
			sorted_inv = OrderedDict(sorted(sorted_inv.items(), key=lambda sorted_inv: sorted_inv[1], reverse=True))
			
	for art, wei in sorted_inv.iteritems():
		print queries +" found in document id= "+str(art)+" with weight = "+str(wei)
			






 
    
