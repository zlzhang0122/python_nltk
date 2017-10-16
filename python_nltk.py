#!/usr/bin/python
#-*- encoding:utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords

response = urllib.request.urlopen("http://www.jd.com/")
html = response.read()
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
clean_tokens = list()
sr = stopwords.words("english")
print (sr)
for token in tokens:
    if token not in sr:
        clean_tokens.append(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print (str(key) + ":" + str(val))
freq.plot(20, cumulative=False)