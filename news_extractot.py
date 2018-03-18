import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# The URL we want to browse to
url = "https://www.reuters.com/news/us"
driver.get(url)

page = driver.find_elements_by_class_name('headline_ZR_Fh')

#for headline in driver.find_elements_by_class_name('headline_ZR_Fh'):
#print(headline.text)

#for date in driver1.find_elements_by_class_name('date-updated_1EZPz'):
#        print(date.text)

#    for data in driver1.find_elements_by_class_name('lede_Wa-ek'):
#        print(data.text)

for i in range(10):
    #page.send_keys(Keys.ENTER)
    time.sleep(3)

    for headline in page:
        print(headline.text)

driver.quit()
