#this tutorial uses selenium to scrape information from mulitple pages using selenium

import csv
from selenium import webdriver

#max number of pages we want to cycle through
MAX_PAGE_NUM = 5
#number of characters in the web url index to cycle through
MAX_PAGE_DIG = 3

with open('result.csv', 'w') as f:
	f.write("Buyers, Price \n")

#start firefox browser and navigate to web page
driver = webdriver.Firefox()

#cylce through webpage according to index numbering
#this will start 001 and cycle to 005
#can be altered by what number we set to MAX_PAGE_NUM and padds appropriate number of zeros
for i in range (1, MAX_PAGE_NUM + 1):
	page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
	url = "http://first_webpage_you_want_to_scrape/" + page_num + ".html"
	#test here
	#print(url)

	driver.get(url)

	buyers = driver.find_elements_by_xpath('//div[@title="buyers-name"]')
	prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

	num_page_items = len(buyers)
	with open('results.csv', 'a') as f:
		for i in range(num_page_items):
			f.write(buyers[i].text + "," + prices[i].text + "\n")

driver.close()			

# driver.get("website URL here")

# #extract lists of buyers and prices based on xpath
# drivers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
# print(buyers)

# prices = driver.find_elements_by_xpath('//span[@class="item-price"]')
# print(prices)

# #print out all of the buyers prices on current page:

# num_page_items = len(buyers)
# for i in range(num_page_items):
# 	print(buyers[i].text + " : " + prices[i].text)

# #clean up close browser window
# driver.close()
