from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
import csv
url1=''
fUrl = ''
rangeLen = 1000
metadata =''
link_array = []
fViews=''
fTags=''
fTitle=''
fThumb=''

#headless
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

#starting gun
url = "https://www.youtube.com/watch?v=2QuI4R16tmc"

for x in range(rangeLen):
    driver.get(url)
    fUrl = url
    time.sleep(2)
    elements = driver.find_elements_by_css_selector("a")
    titles = driver.find_elements_by_css_selector("meta")
    views = driver.find_elements_by_css_selector("span")
    for view in views:
        if(str(view.get_attribute("class"))=="view-count style-scope yt-view-count-renderer"):
#            print(view.text)
            fView = view.text
    
    thumbnails = driver.find_elements_by_css_selector("link")
    for thumbnail in thumbnails:
        if(str(thumbnail.get_attribute("itemprop"))=="thumbnailUrl"):
#            print(thumbnail.get_attribute("href"))
            fThumb = thumbnail.get_attribute("href")
   
    keywords = driver.find_elements_by_css_selector("meta")
    for keyword in keywords:
        if(str(keyword.get_attribute("name"))=="keywords"):
#            print(keyword.get_attribute("content"))
            fTags = keyword.get_attribute("content")
    
    for title in titles:
        if(str(title.get_attribute("itemprop"))=="name"):
#            print(title.get_attribute("content"))
            fTitle = title.get_attribute("content")
    
    for element in elements:
        url1 = element.get_attribute("href")
        if ('https://www.youtube.com/watch?v') in str(url1):
            link_array.append(url1)
    url = random.choice(link_array)
    link_array.clear()
    print(str(x)+"/"+str(rangeLen))
    with open('youtube-pull-new.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fTitle, fView, fTags, fThumb, fUrl])
#    print(random.choice(link_array))


driver.close()

