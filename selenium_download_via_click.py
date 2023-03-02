from selenium import webdriver

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

browser = webdriver.Firefox(profile)
browser.get("https://images.nasa.gov/details-PIA03606.html")

#browser.findElement(By.id("btn btn-default btn-lg dropdown-toggle")).click();
browser.find_element_by_class_name('detail-download btn-group').click()
