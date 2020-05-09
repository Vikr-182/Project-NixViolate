import requests,sys,webbrowser,bs4
import urllib
import re
import time
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
import sys 

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
chrome_options = Options()  
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

url = sys.argv[1]
timeout=10
count=0

driver = webdriver.Chrome(executable_path=r"./chromedriver",chrome_options=chrome_options)
driver.get(url)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(timeout)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    count=count+1
    print(count)
r = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(r,'html.parser')


print(soup.text)

print("##links##")

for link in soup.find_all('a'):
    if link.has_attr('href'):
        if len(link['href']):
            if link['href'][0] == "/":
                print("https://summerofcode.withgoogle.com"+link['href']) 
            else :
                print(link['href'])


print(count)
