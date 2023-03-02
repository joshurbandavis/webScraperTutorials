#use Beautiful Soup to download images in this tutorial
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#setting up
def make_soup(url):
	thepage=urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soup data

i = 1

soup = make_soup("https://website here")
for img in soup.findAll('img'):
	temp=img.get('src')
	if temp[:1]=="/":
		image = "https://base_of_website_stub" + temp
	else:
		image = temp	

	nametemp = img.get('alt')
	if len(nametemp)==0:
		filename=str(i)
		i=i+1
	else:
		filename=nametemp

	imagefile = open(filename + ".jpeg", 'wb')
	imagefile.write(urllib.request.urlopen(image).read())
	imagefile.close()
