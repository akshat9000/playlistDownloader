# playlistDownloader
A simple python script which enables you to download multiple videos of a playlist, either manually created or pre-made

## Aim
I aim to create a python script which works in tandem with a txt file located in the same directory, which contains a list of urls.
This will be different from the other downloaders which exist as the user will have the option of either simply creating a list of videos to download by copying its urls onto the txt file, or just copying the url of the first video of a pre-existing playlist, and the script will do the rest

## How to use?
This script is fairly simple to use.
Just download the python file along with the urls.txt file to a location of your choice on you machine,
list all the urls of the videos you require to be downloaded,
open up a terminal instance, navigate to the folder where you have kept this file, and simply execute the python script.

<s>*Note: This is **NOT** the headless version, that is soon to follow, meanwhile, you can choose to minimize the window that pops up, or watch it download*</s>

*This **IS** the headless version, enjoy!*

## Dependencies
### These are the features you will definitely require
* [Python, version 2 or above](https://www.python.org/)
* [Selenium Webdriver](https://www.selenium.dev/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Chromedriver](https://chromedriver.chromium.org/), but if you dont have it, the script auto-downloads it for you!

## Right Now
As of this moment, this script only works on [vidmo.org](vidmo.org), as the location of the specific url source from the specific video tag is unique only to this site, and this script is based solely upon webscraping, but I am trying to make a generic downloader too!
