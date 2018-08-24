
def getCritic(review):
    critic='NA'
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: critic=criticChunk.text#.encode('ascii','ignore')
    return critic

def getRating(review):
    rating = 'NA' #Initailize rating to NA
    if (review.find('div',{'class':'review_icon icon small fresh'})):
        return ('fresh')
    elif (review.find('div',{'class':'review_icon icon small rotten'})):
        return ('rotten')
    else:
        return rating
        
def getSource(review):
    Sorcc='NA'
    Sorc=review.find('em',{'class':"subtle"})
    if Sorc: Sorcc=Sorc.text
    return Sorcc
    
def getDate(review):
    Dat='NA'
    Dat=review.find('div',{'class':"review_date subtle small"})
    if Dat: Datt=Dat.text
    return Datt
    
def getTextLen(review):
    TotLen='NA'
    textChunk=review.find('div',{'class':'the_review'})
    if textChunk: text=textChunk.text#.encode('ascii','ignore')	
    TotLen= len(text)                
    return TotLen

def run(url):

    pageNum=1 # number of pages to collect

    fw=open('reviews.txt','w') # output file
	
    for p in range(1,pageNum+1): # for each page 

        print ('page',p)
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        global reviews
        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs
        for review in reviews:  
            #critic,Sorcc,Datt,TotLen='NA','NA','NA','NA'
            Sorcc=getSource(review)
            critic=getCritic(review)
            rating=getRating(review)
            Datt=getDate(review)
            TotLen=getTextLen(review)
            
            fw.write(critic+'\t'+rating+'\t'+Sorcc+'\t'+Datt+'\t'+str(TotLen)+'\n') # write to file 
		
            #time.sleep(2)	# wait 2 secs 
      
    fw.close()


    
if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)