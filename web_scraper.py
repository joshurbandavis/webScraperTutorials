#Note: to be ran with Python 3 
#May need to install anaconda for Python 3
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://yoururlhere'

#open connection and grabbing webpage
uReq(my_url)
uClient = uReq(my_url)

#offload content into variable
page_html = uClient.read()
uClient.close()

#parse html into datatype soup from beautiful soup
page_soup = soup(page_html, "html.parser")

#grabs first header and print
#page_soup.h1 

#traverse html by tag (requires inspecting page elements for specificity)
#page_soup.body.span

#function to grab all items
containers = page_soup.findAll("div",{"class":"item-container"})

#how many did we find?
len(containers)

#note: use JSBeauifier to clean up messy html code that you want to read. 
#this is helpful for exploring the above functions

container = containers[0]

#create file to write
filename = "products.csv"
f = open(filename, "w")

#note:csv files deliminated by new line
headers = "brand, product_name, shipping\n"


for container in containers:
	#example image item with tag "title" which can be scraped
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	#strip function can be used to remove excess spacing from scraped text
	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	#be sure to check that your strings are clean
	#if not, use the replace fucntion: product_name.replace(",", "|")
	f.write(brand + "," + product_name + "," + shipping + "\n")

	#container.div.div.a.img["title"]
