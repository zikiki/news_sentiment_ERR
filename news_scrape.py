import time
import csv
import selenium.webdriver.support.ui as ui

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("https://www.reuters.com/news/us")
time.sleep(5)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 50

while no_of_pagedowns:
    
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

main_window = browser.current_window_handle
post_headlines = browser.find_elements_by_class_name('headline_ZR_Fh')

with open('/Users/roliesha/news_currency/news.csv', 'w') as f_output:
    writer = csv.DictWriter(f_output, fieldnames = ["Date", "Title", "Summary"], delimiter=',')
    writer.writeheader()

    for headlines in post_headlines:
    
        first_link = headlines.find_element_by_tag_name('a')
        first_link.send_keys(Keys.COMMAND + Keys.RETURN)
        time.sleep(5)
        browser.switch_to_window(browser.window_handles[1])
    
        time.sleep(0.5)
    
        date = browser.find_element_by_class_name("date_V9eGk")
        #print(date.text)

        head = browser.find_element_by_class_name("headline_2zdFM")
        #print(head.text)

        summary = browser.find_element_by_class_name("first-p_2htdt")
        #print(summary.text)

        writer.writerow({"Date":date.text, "Title":head.text, "Summary":summary.text})

        browser.close()
        time.sleep(0.5)
        browser.switch_to_window(main_window)

browser.quit()
