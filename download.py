from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import os
import os.path

if(not os.path.isdir('Downloads')):
    os.mkdir('Downloads')
    print('made local Downloads folder')
    time.sleep(0.5)

execPath = '{}\\chromedriver'.format(os.getcwd())
print('chromedriver executable path: '+execPath)
time.sleep(0.5)
downPath = '{}\\Downloads'.format(os.getcwd())
print('download destination: '+downPath)
time.sleep(0.5)

opts = Options()
print('customizing broswer')
time.sleep(0.5)
opts.add_argument('--verbose')
print('1. verbose')
time.sleep(0.5)
opts.add_argument('--headless')
print('2. headless')
time.sleep(0.5)
opts.add_argument('--no-sandbox')
print('3. no sandbox')
time.sleep(0.5)
opts.add_argument('--disable-gpu')
print('4. disable gpu')
time.sleep(0.5)
opts.add_argument("--window-size=1920x1080")
print('5. set window size')
time.sleep(0.5)
opts.add_argument("--disable-notifications")
print('6. disable notifications')
time.sleep(0.5)
opts.add_argument('--disable-software-rasterizer')
print('7. disable software rasterizer')
time.sleep(0.5)
opts.add_experimental_option("prefs", {
        "download.default_directory": downPath,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
print('adding experimental options')
time.sleep(0.5)
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
print('adding user agents')
time.sleep(0.5)

def enable_download_headless(browser):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': downPath}}
    browser.execute("send_command", params)

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
	return st2

def down():
    ls = blobsAll()
    for url in ls:
        du = getLink(url)
        st2 = createName(du)
        if(os.path.isfile('{}\\{}.mp4'.format(downPath,st2))):
            print(st2+' already exists')
            continue
        browser.get(du)
        while(not os.path.isfile('{}\\{}.mp4'.format(downPath,st2))):
            print('downloading '+st2+' . . .')
            time.sleep(30)
        print('done downloading '+st2)
        print('*****************')
    print('all tasks completed')

        
time.sleep(0.5)
print('initializing browser')
browser = webdriver.Chrome(executable_path=execPath,options=opts)
enable_download_headless(browser)
time.sleep(0.5)
print('starting download')
time.sleep(0.5)
print('*****************')
down()
browser.quit()
print('**********************************************************')
print('*                Thanks for using my app                 *')
print('*         for more details, visit my github repo         *')
print('*    https://github.com/akshat9000/playlistDownloader    *')
print('**********************************************************')
