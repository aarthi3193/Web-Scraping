# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:46:09 2017

@author: AWESOME JESUS
"""
from bs4 import BeautifulSoup
import re
import time
import requests


def getTime(review):
    timeeee='NA'
    timees=review.find('a',{'class':'biz-name js-analytics-click'})
    timee=timees['href']
    pageurl='https://www.yelp.com'+timee
    for i in range(5):
        try:
            #use the browser to access the url
            response=requests.get(pageurl,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            html=response.content # get the html
            break # we got the file, break the loop
        except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
            print ('failed attempt',i)
            #time.sleep(2) # wait 2 secs
            if not html:
                continue
        
    soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
    timeee=soup.find('strong',{'class':'u-space-r-half'})
    #timeee=soup.find('dd',{'class':'nowrap price-description'})
    #if timeee:
    timeeee=timeee.text
    return timeeee        
    
    
def getName(review):
    name='NA'
    names=review.find('a',{'class':'biz-name js-analytics-click'})
    if names:
        name=names.text
    return name

def getrating(review):
    Rating='NA'
    ratings=review.find('div',{'class':re.compile('i-stars')})
    if ratings:
       Rating=ratings['title']
    return Rating

def run(url):
    pageNum=00
    fw=open("yelp.txt",'w')
    for p in range(00,pageNum+10,10):
        print ('Page: ', p)
        html=None
        pagelink=url+str(p)+'&cflt=restaurants'
        #print (pagelink)
        for i in range(5):
            try:
                #use the browser to access the url
                response=requests.get(pagelink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                #time.sleep(2) # wait 2 secs
        if not html:
            continue
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        reviews=soup.findAll('div', {'class':re.compile('natural-search-result')}) # get all the review divs
        for review in reviews:
            name=getName(review)
            rating=getrating(review)
            timing=getTime(review)
            #norat=getnumb(review)
            #address=getadd(review)
	
            fw.write(name+'\t'+str(timing)+'\t'+str(rating)+'\n') # write to file 
            break		
            #time.sleep(0.5)	# wait 2 secs 

    fw.close()

if __name__=='__main__':
    url='https://www.yelp.com/search?find_desc=Restaurants&find_loc=New+York%2C+NY&ns=1'
    run(url)
    
    
"""
      
def runprg(url):
    Name='NA'
    Fact='NA'
    Reviewer='NA'
    Header='NA'
    Review='NA'
    Result='NA'
    fw=open('poliall.txt','w')
    getFacts(url,'true')
    fw.write(Name+'\t'+Fact+'\t'+Reviewer+'\t'+Header+'\t'+Review+'\t'+Result+'\n\n')
    
    
runprg('http://www.politifact.com/truth-o-meter/rulings/')

"""