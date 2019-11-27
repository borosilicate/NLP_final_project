import requests
import bs4
import time
#open communion.txt
#load words
agency_ranking=''
classes=['css-gkae64 etbu2a31','css-q7ic04 etbu2a31','css-zu4egz etbu2a31']
with open('communion_words.txt','r') as f:
    words=f.readlines()
for w in words:
    time.sleep(3)
    o=requests.request('get',url='https://www.thesaurus.com/browse/'+w+'?s=t') 
    soup=bs4.BeautifulSoup(o.text,'html.parser') 
    for i,c in enumerate(classes): 
        for s in soup.find_all('a',class_=c): 
            if('%' not in s.get('href') and '-' not in s.get('href')): 
                l=s.get('href').split('/') 
                l=l[len(l)-1] 
                print(l,1-i*0.15) 
                agency_ranking+=' '+str(1-i*0.15)+' '+l+'\n'

print(agency_ranking)
with open('communion_rankings.txt','w+') as fil:
    fil.write(agency_ranking)
    fil.close()
