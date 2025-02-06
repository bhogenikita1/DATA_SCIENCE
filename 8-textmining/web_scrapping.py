# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 08:25:17 2024

@author: HP
"""

#WEB SCRAPPING

from bs4 import BeautifulSoup
import requests
soup=BeautifulSoup(open("C:/8-textmining/textmining/sample_doc.html"),'html.parser')
soup


#it is going to show all the html content extracted
soup.text
#It will show only text
soup.contents
#It will show only text
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
soup


for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)
    
#It will show all the rows except first row
#Now we want to display M.tech which is located in third row
#i need  to give [3][2]
table.find_all('tr')[3].find_all('td')[2] # <td>M.Tech</td>
table.find_all('tr')[4].find_all('td')[1] # <td>B.Music</td>

from bs4 import BeautifulSoup as bs
link="https://sanjivanicoe.org.in/index.php/contact"
page=requests.get(link)
page
# response [200]> it means connection is establish successful
page.content
#you will get all html source code but very crowdy text
#let us apply html parser
soup = bs(page.content,'html.parser')
soup

#Now the text is clean but not up to the expectations
#now let us apply prettify method

print(soup.ptettify)
#the text is neat and clean
list(soup.children)
#finding all contents using tab
soup.find_all('p')

#ex1
import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://www.amazon.in/gp/aw/d/B0CQD25FY4/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=350b61c2114a56fee0d02a1df4b42590&hsa_cr_id=0&qid=1724990822&sr=1-2-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_sccd_asin_1_img&pd_rd_w=ecxwp&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_p=df9fe057-524b-4172-ac34-9a1b3c4e647d&pf_rd_r=V0SRA9VK253E0W229TEG&pd_rd_wg=xVHVQ&pd_rd_r=ead17416-2bd3-4873-8f48-8d161b489e2f&th=1"
page=requests.get(link)
page
page.content

#Now let us parse the html page
soup= bs(page.content,'html.parser')
soup

#now lets scrap the content
names=soup.find_all('span',class='')


print(soup.prettify)
list(soup.children)
soup.find_all('p')


######  2/09/2024  ###### 

import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://www.amazon.in/product-reviews/B01EZ0X55C/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar"
page=requests.get(link)
page
page.content
## now let us parse the html page
soup=bs(page.content,'html.parser')
print(soup.prettify())
#when you parse HTML using BeautifulSoup, you are converting the 
#raw HTML content of a web page into a structured format, 
#like a tree, where you can easily locate and manipulate individual 
#elements (such as tags, attributes, or text).

#page.content=> provides the raw HTML content,
#while soup.prettify()=> offers a formatted, human-readable version of the parsed HTML content.

## now let us scrap the contents
names=soup.find_all('span',class_='a-profile-name')
names
### but the data contains with html tags,let us extract names from html tags
cust_names=[]
for i in range(0,len(names)):
    cust_names.append(names[i].get_text())
    
cust_names
len(cust_names)
cust_name1=[]

for i in cust_names:
    if i not in cust_name1:
        cust_name1.append(i)
cust_name1
len(cust_name1)
cust_name1.pop(-1)
### There are total 11 users names 
#Now let us try to identify the titles of reviews
title=soup.find_all('a',class_='review-title')
title
# when you will extract the web page got to all reviews rather top revews.when you
# click arrow icon and the total reviews ,there you will find span has no class
# you will have to go to parent icon i.e.a
#now let us extract the data
review_titles=[]
for i in range(0,len(title)):
    review_titles.append(title[i].get_text())

review_titles
# ouput we will get consists of \n 
review_titles=[ title.strip('\n')for title in review_titles]
review_titles
len(review_titles)
##now let us scrap ratings
rating=soup.find_all('span',class_='a-icon-alt')
rating
###we got the data
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)   
rate1=[]

   
rate.pop(-1)
rate.pop(-1)
rate.pop(-1)
rate.pop(-1)
rate.pop(-1)
rate.pop(-1)
len(rate)
## now let us scrap review body
reviews=soup.find_all("span",class_='a-size-base review-text review-text-content')
reviews
review_body=[]
for i in range(0,len(reviews)):
    review_body.append(reviews[i].get_text())
review_body
review_body=[ reviews.strip('\n\n')for reviews in review_body]
review_body
len(review_body)
##########################################
###convert to csv file
import pandas as pd
df=pd.DataFrame()
df['customer_names']=cust_name1
df['review_title']=review_titles
df['rate']=rate
df['review_body']=review_body
df
df.to_csv('c:/360DG/Assignments/Text-minning/Amazon_reviews.csv',index=True)
########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("c:/360DG/Assignments/Text-minning/Amazon_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']


import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://www.imdb.com/title/tt0068646/reviews?ref%20=tt_urv"
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify)

title=soup.find_all('a',class_="title")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:]=[title.strip('\n')for title in review_title]
review_title
len(review_title)    
#we got 25 review titles

##now let's srcap rating

rating=soup.find_all('span',class_="point-scale")
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('/')for r in rate]
rate
len(rate)
rate.append('')
rate.append('')
len(rate)#25
#rate.pop(-1)
#rate.pop(-1)
len(rate)#23


##Now let us scrap the review body

review=soup.find_all('div',class_='text show-more__control')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)
##we got 25 review body
#now we have to save data in csv file

import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['Rate']=rate
df['Review']=review_body
df

df.to_csv("C:/8-textmining/textmining/GodFather_reviews.csv")
df

###pip install textblob
#1=>+ve sentiment
#0=>-ve sentimant
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("C:/8-textmining/textmining/GodFather_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']

'''
Sentiment Analysis: One of the most common uses of TextBlob is for sentiment analysis. 
It can analyze a piece of text and return its polarity (how positive or negative it is) 
and subjectivity (whether the text is factual or opinion-based).
Polarity: Ranges from -1 (negative sentiment) 
                    to +1 (positive sentiment).
'''



from bs4 import BeautifulSoup
import requests
soup=BeautifulSoup(open("C:/8-textmining/textmining/sample_doc.html"),'html.parser')
soup










