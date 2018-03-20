import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("https://www.reuters.com/news/us")
time.sleep(5)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 5

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

post_headlines = browser.find_elements_by_class_name('headline_ZR_Fh')

for headlines in post_headlines:
    print(headlines.text)


browser.quit()
