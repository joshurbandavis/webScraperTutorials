from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

file = open('NYTobitfile.txt','w+') 


url = ("https://www.nytimes.com/section/obituaries")

#print(url)
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

for link in soup.find_all('a'):
	print(link.get('href'))
	file.write(link.get('href'))
	file.write('\n')

