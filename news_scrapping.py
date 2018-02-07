import requests
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.reuters.com/news/us"
driver.get(url)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight
driver.execute_script("window.scrollTo(0, 10000000);")

time.sleep(5)
find_element_by_css_selector('h2.FeedItemHeadline_headline_ZR_Fh')
headlines = driver.find_element_by_class_name("FeedItemHeadline_headline_ZR_Fh")
for headline in headlines:
    print(headline.get_attribute("href"))
i = 0
for element in headlines:
    headline_url = element.get_attribute("href")
    # Send an HTTP GET request, get and save the image from the response
    image_object = requests.get(image_url)
    image = Image.open(BytesIO(image_object.content))
    image.save("./images/image" + str(i) + "." + image.format, image.format)
    i += 1
