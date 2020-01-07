#!/usr/bin/env python
import urllib
import os
from bs4 import BeautifulSoup

cwd = os.getcwd()

if __name__ == '__main__':

	if not os.path.exists(cwd + "/articles"):
    		os.makedirs(cwd + "/articles")
    # Build Inverted-Index for documents
	with open("urls", "r") as fh:
		i = 0
		for url in fh:
			i+=1
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html)

			# kill all script and style elements
			for script in soup(["script", "style"]):
			    script.extract()    # rip it out

			# get text
			text = soup.get_text()
			# break into lines and remove leading and trailing space on each
			lines = (line.strip() for line in text.splitlines())
			# break multi-headlines into a line each
			chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
			# drop blank lines
			text = '\n'.join(chunk for chunk in chunks if chunk)
			text = text.encode("utf-8")
			text = text.lower()
			print(text)				
			completeName = os.path.join(cwd+"/articles", "article" + str(i)+".txt") 
			with open(completeName,'w') as f:
				f.write(text)













