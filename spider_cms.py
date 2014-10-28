#!/usr/bin/env python
#coding:utf8
'''
spider the hacker "雨`" fucked CMS
@author: bkwy.org
'''
import os
import re       
import urllib2
allCms=set('')  

def geturl(id):
    url = "http://www.wooyun.org/whitehats/%E2%80%B2%20%20%E9%9B%A8%E3%80%82/type/1/page/" + str(id)
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    http = res.read()
    r = '<td><a href="(\S+)" target="_blank">(\w+|\S+)'

    r=re.compile(r)
    p=r.findall(http)
    for i in range(len(p)):
        allCms.add(urlreplace(p[i][1]).upper())
    

def urlreplace(url):
    url=url.replace('http://','')
    url=url.replace('www.','')
    url=url.replace('/','')
    url=url.replace('<a>','')
    return url

def getCms():
    i = 0
    while i < 8:
        geturl(i+1)
        i += 1

    listCms = ['']
    for cms in allCms:
        listCms.append(cms)
    listCms.sort()
    return listCms
    

if __name__ == '__main__':
    listCms = getCms()
    print 'CMS About:', len(listCms)
    for cms in listCms:
        print cms 
        
    op = raw_input('save it to the file ? (y/n)\n>')
    if op.lower() == 'y':
        fileName = raw_input('Please input the file name !\n>')
        if fileName.find('.') == -1:
            fileName += '.txt'
        path = os.getcwd()
        file = open(fileName, 'w')
        for cms in listCms:
            file.write(cms+'\n')
        file.close()
        print ' The file is saved in:', path, fileName
  
