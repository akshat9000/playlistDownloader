from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os
import os.path

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
browser = webdriver.Chrome(executable_path='C:\\Users\\Akshat Srivastava\\Downloads\\chromedriver',options=opts)

dpath = 'C:\\Users\\Akshat Srivastava\\Downloads\\'

def getURLlist():
    lines = open('urls.txt','r').read().splitlines()
    return lines

def blobsAll():
    lis = getURLlist()
    bl = []
    for i in lis:
        bl.append(i)
    return bl

def getLink(url):
	browser.get(url)
	return browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[6]/div/video').get_attribute('src')

def createName(st2):
	st2 = st2.split('/')[-1].split('.')[0][10:]
	st = dpath + st2 + '.mp4'
	return st2, st

def down():
	ls = blobsAll()
	for url in ls:
		du = getLink(url)
		st2, st = createName(du)
		browser.get(du)
		while(not os.path.isfile(st)):
			print('downloading '+st2+' . . .')
			time.sleep(30)

down()
browser.quit()
