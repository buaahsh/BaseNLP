# -*- coding:utf-8 -*-

'''
Created on Jan 26, 2015

@author: v-yunlma
'''


import urllib
import time
import getopt
import sys
# import urllib2

from selenium import webdriver


def download(inputFile, inputFile2, engine):
    reader = open(inputFile, "r")     
    browser = webdriver.Firefox()
    qid = -1
    for line in reader:
        items = line.split("\t")
#         qid = int(items[0].strip())
#         question = items[1].strip()
        qid += 1
        question = items[0].strip()
        url = build_url(question, engine)
        print("[LOG] - qid:" + str(qid) + " - url:" + url)
        download_url(browser, qid, url, question, inputFile2)
#     browser.quit()
    return


def build_url(question, engine):
    google_prefix = "http://www.google.com/search?gws_rd=ssl&ie=utf-8&oe=utf-8&q="
    bing_prefix = "http://www.bing.com/?setmkt=en-US&setlang=en&q="
    prefix = None
    if(engine == "google"):
        prefix = google_prefix
    elif(engine == "bing"):
        prefix = bing_prefix
    else:
        return None
        
    return prefix + urllib.parse.quote(question)


def save(fileName, qid, url, html):
    # html = html.encode('utf-8')
    start_label = "<body"
    end_label = "</body>"
    html = start_label + html.split(start_label)[1].split(end_label)[0] + end_label
    writer = open(fileName, "a", encoding="utf-8")
    writer.write(str(qid) + "\n")
    writer.write(url + "\n")
#     writer.write(html + "\n")
    writer.write(html.replace("\n", "").replace("\r", "").replace("\t", " ") + "\n")
    writer.close()
    return


def download_url(browser, qid, url, question, inputFile):
    browser.implicitly_wait(15)
    browser.get(url)
    html = browser.page_source
    time.sleep(3)
    save(inputFile , qid, url, html)
    return


if __name__ == "__main__":
    try:  
        shortargs = 'q:'
        longargs = ['site=']
        opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)
    except:  
        sys.exit(2)
    
    htdoc_file = "temp.txt"
    trigger_file = ".htdoc"
    site = "google";
    for o, a in opts:
        if o == "-q":
            htdoc_file = a
        elif o == "--site":
            site = a
        else:
            pass
    trigger_file = (htdoc_file[:-4] if(htdoc_file[-4:] in (".txt", ".tsv", ".csv"))else htdoc_file) + ".htdoc"
 
    download(htdoc_file, trigger_file, site)
    
    print("Successfully finished!")
