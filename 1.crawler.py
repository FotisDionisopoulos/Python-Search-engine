#!/usr/bin/env python
import urllib2
import os
from BeautifulSoup import BeautifulSoup
stri =0 
cwd = os.getcwd()
start_urls = [
	'https://www.catersnews.com/stories/latest-news/page/1/',
	'https://www.catersnews.com/stories/latest-news/page/2/',
    ]


if __name__ == '__main__':
	if not os.path.exists(cwd + "/html_code"):
    		os.makedirs(cwd + "/html_code")
	with open('urls', 'w') as fh:
		for url in start_urls:
			text = urllib2.urlopen(url).read()
			soup = BeautifulSoup(text)
			productDivs = soup.findAll('div', attrs={'class' : 'one-half block__media text__block left--float'})
	
			for div in productDivs:
				print div.a['href']
				fh.write(div.a['href']+ "\n")
				stri +=1
				completeName = os.path.join(cwd+"/html_code", "file" + str(stri)+".html") 
				file(completeName, "w").write(urllib2.urlopen(div.a['href']).read())


