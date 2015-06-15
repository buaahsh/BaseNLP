__author__ = 'hsh'


import urllib
import time
import getopt
import sys
import random
# import urllib2

from selenium import webdriver

class WebScraper():

    def __init__(self, isSleep=True):
        self.__browser = webdriver.PhantomJS()
        self.__sleepTime = 0
        if isSleep:
            self.__sleepTime = random.random() * 3


    def downloadPage(self, url):
        self.__browser.implicitly_wait(15)
        self.__browser.get(url)
        html = self.__browser.page_source
        time.sleep(self.__sleepTime)
        return html

if __name__ == "__main__":
    ws = WebScraper()
    url = "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6%E7%9A%84%E8%80%81%E5%A9%86%E6%98%AF%E8%B0%81"
    html = ws.downloadPage(url)
    print html