from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

file = open('testfile.txt','w+') 

pages = []

for i in range(3):
	url = ("http://oa.anu.edu.au/obituaries/death/?page=" + 'x' + "&sortOrder=desc")
	r  = requests.get(url)

	data = r.text

	soup = BeautifulSoup(data)

	for link in soup.find_all('a'):
		print(link.get('href'))
		pages.append(link.get('href'))


# for item in pages:
# 	page = request.get(item)
# 	soup = BeautifulSoup(page.text, 'html.parser')

# 		# here, we fetch the content from the url, using the requests library
# 		page_content = BeautifulSoup(r.content, 'html.parser')
# 		#we use the html parser to parse the url content and store it in a variable.
# 		textContent = []

# 		for j in range(3):
# 			paragraphs = page_content.find_all('p')[j].text
# 			textContent.append(paragraphs)

# 		file.write(paragraphs)

# file.close()