from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

file = open('obituary_text_corpus.txt','w+') 
#url_list = open('obituary_urls.txt', 'r')

with open('obit_links.txt') as lines:
	for line in lines:
		#line = x.readline()

		next_url = ("http://oa.anu.edu.au" + line)
		print (next_url)

		r  = requests.get(next_url)

		#data = r.text

		#soup = BeautifulSoup(data)

		# here, we fetch the content from the url, using the requests library
		page_content = BeautifulSoup(r.content, "html.parser")
		#we use the html parser to parse the url content and store it in a variable.
		textContent = []

		name = page_content.find('h2').text
		textContent.append(name)
		file.write(name)
		file.write("\n")

		for j in range(0, 20):
			paragraphs = page_content.find_all("p")[j].text
			textContent.append(paragraphs)

			if(j>=1):
				file.write(paragraphs)

		file.write("\n")		


# #url = ("http://oa.anu.edu.au" + "/obituary/inder-stuart-gerald-19837")
# 	print(next_url)
# 	r  = requests.get(next_url)

# 	data = r.text

# 	soup = BeautifulSoup(data)

# # here, we fetch the content from the url, using the requests library
# 	page_content = BeautifulSoup(r.content, "html.parser")
# #we use the html parser to parse the url content and store it in a variable.
# 	textContent = []

# 	name = page_content.find('h2').text
# 	textContent.append(name)
# 	file.write(name)
# 	file.write("\n")

# 	for j in range(0, 20):
# 		paragraphs = page_content.find_all("p")[j].text
# 		textContent.append(paragraphs)

# 		if(j>=1):
# 			file.write(paragraphs)

# 	file.write("\n")		

# file.close()