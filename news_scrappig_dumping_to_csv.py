import csv
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def get_elements_by_class(driver, class_name):
    return [entry.text.encode('ascii', 'ignore') for entry in driver.find_elements_by_class_name(class_name)]


url = ("https://www.reuters.com/news/us")
driver = webdriver.Chrome()
driver.get(url)


time.sleep(5)

elem = driver.find_element_by_tag_name("body")

no_of_pagedowns = 100

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1


search_entries = [
    ("Summary", "lede_Wa-ek"),
    ("Title", "headline_ZR_Fh")
    ]

with open('/Users/ziqizang/Documents/news_sentiment_ERR-master/news2.csv', 'w') as f_output:
    csv_output = csv.writer(f_output)
    # Write header
    csv_output.writerow([name for name, class_name in search_entries])
    entries = []
    for name, class_name in search_entries:
        entries.append(get_elements_by_class(driver, class_name))
        csv_output.writerows(zip(*entries))


driver.quit()
