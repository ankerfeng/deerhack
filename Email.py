#!/usr/bin/env python
# coding=utf-8
'''
Created on 2014年12月6日

@author: bkwy.org
'''
import re
import urllib2
from urllib import urlopen


def GetUrl():
    urls = []
    word = 'A'
    i=0
    while i < ord('Z')+1: 
        urls.append("http://homepage.hit.edu.cn/names/"+chr(ord(word)+i))
        #print "http://homepage.hit.edu.cn/names/"+chr(ord(word)+i)
        i += 1
    return urls

def Purl(urladdr):
    http = urlopen(urladdr)
    #print http.read()
    http = http.read()
    regex = re.compile(r'"/pages/.+?"')
    theUrls = regex.findall(http)
    i = 0
    while i < len(theUrls):
        theUrls[i] = theUrls[i].replace('"', '')
        #print theUrls[i]
        i += 1
    return theUrls
       
def Email(urladdr):
    f = open('email.txt', 'a')
    http = urlopen(urladdr)
    #print http.read()
    http = http.read()
    regex = re.compile(r'<a href="mailto:.+?">.+?</a></td>')
    theEmails = regex.findall(http)
    for theEmail in theEmails:
        regex = re.compile(">.+?<")
        theEmail = regex.findall(theEmail)
        theEmail = theEmail[0].replace('>', '')
        theEmail = theEmail.replace('<', '')
        f.write(theEmail+'\n')
        print theEmail
    f.close()
    
        
if __name__ == '__main__':
    f = open('email.txt', 'a')
    f.write("=====================\n")
    f.close()
    urls = GetUrl()
    for url in urls:
        print url
        theUrls = Purl(url)
        for purl in theUrls:
            print purl
            Email("http://homepage.hit.edu.cn"+purl)
