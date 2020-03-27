import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import html5lib
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")

# browser = webdriver.Chrome(executable_path='C:\\Users\\Akshat Srivastava\\Downloads\\chromedriver',options=chrome_options)
browser = webdriver.Chrome(executable_path='C:\\Users\\Akshat Srivastava\\Downloads\\chromedriver')

url1 = 'https://www.youtube.com/watch?v=bytnxnZFLeg'

def getBlob(url):
	browser.get(url)
	soup = BeautifulSoup(browser.page_source,'html.parser')
	blob = soup.find('video',{"src":True})
	return blob['src']

def getURLlist():
	lines = open('urls.txt','r').read().splitlines()
	return lines

def blobsAll():
	lis = getURLlist()
	bl = []
	for i in lis:
		bl.append(getBlob(i))
	print(bl)
	browser.quit()

blobsAll()
