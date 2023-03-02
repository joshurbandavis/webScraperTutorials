from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

file = open('NYTobitfile.txt','w+') 

for i in range(1, 299):
	url = ("https://www.nytimes.com/interactive/2015/obituaries/notable-deaths-2015.html#modal/%s") % i
	r  = requests.get(url)

	data = r.text

	soup = BeautifulSoup(data)

	for link in soup.find_all('a'):
		print(link.get('href'))
		file.write(link.get('href'))
		file.write('\n')