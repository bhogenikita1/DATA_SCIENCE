# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:11:13 2024

@author: NIKITA
"""

########## 12/06/2024 ###############

#PYTHON FOR NLP = NATURAL LANGUAGE PROCESSING
#   WEB SCRAPPING
#1) DATA AQUISITION
#2) TEXT EXTRACTION AND CLEAN UP 
#3) PRE_PROCESSING
#4) FEATURE ENGINEERING=EXTRACTING FEATURES FROM RAW DATA
#5) MODEL BUILDING
#6) EVALUATION
#7) DEPLOYMENT
#8) MONITOR AND DEPLOYMENT

 
#####  TEXT MINING  #####

sentence="we are learning TextMining from Sanjivani AI"

##IF WE WANT TO KNOW POSITON OF LEARNING
sentence.index("learning")
#LEARNING IS AT 7TH POSITION
##IF WE WANT TO KNOW POSITON OF Textmining
###SPLIT DO THE  TOKENIZATION(SEPARATE(choping the sentence) THE SENTENCE INTO WORDS)

sentence.split().index("learning")
sentence.split().index("TextMining")

###IT WILL SPLIT THE WORDS IN LIST AND COUNT THE POSITION
######### PRINITNG ANY WORD IN REVERSE ORDER
sentence.split()[2][::-1]

##[START:END END:-1(START)] WILL START FROM -1,-2,-3
##printing the first and last word
words=sentence.split()
words
first_word=words[0]  #'we'
first_word
last_word=words[-1]  #'AI'
last_word

##concatting the first and last word
concat_word=first_word+""+last_word
concat_word

###printing the even words from the sentence
[words[i] for i in range(len(words))if i%2==0]
###words having odd length will not be printed
[words[i] for i in range(len(words))if i%2==1]
sentence
#want to display AI
sentence[-3:]
#it will start from -3 ,-2,-1 i.e.AI
sentence[-2:]

######reverse the sentence
words=sentence.split()
words[::-1]
['AI', 'Sanjivani', 'from', 'TextMining', 'learning', 'are', 'we']


#printing entire sentence in reverse order
sentence[::-1]
#'IA inavijnaS morf gniniMtxeT gninrael era ew'

##suppose we want to select each word and print in reversed



words
print( " ".join(word[::-1]for word in words))
#it will display==> ew era gninrael gniniMtxeT morf inavijnaS IA
 
##tokenisation
#CHOPPING THE SENTENCE INTO WORDS
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
 
#parts of speech (pos)tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
#it is mentioning parts of speech
#[('I', 'PRP'),=PRP=pronoun
 #('am', 'VBP'),
 #('reading', 'VBG'),
 #('NLP', 'NNP'),
 #('Fundamentals', 'NNS')]
#stop words from NLTK library
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=stopwords.words('English')
print(stop_words)

##########13/06/2024##########

#LET US FILTER THE SENTENCE USING STOP_WORDS
sentence_words=" i am a student of sanjivani college of engineering"
sentence_no_stops=" ".join([words for words in sentence_words ])
print(sentence_no_stops)

##you can notice that am,is.of the most popular,in are missing
##########
#suppose we want to replace words in string
sentence2="I visited NY from IND on 14-02-19"
normalized_sentence=sentence2.replace("NY","Malaysia")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

from autocorrect import Speller
spell=Speller(lang='en')
spell("Engilish")

#############################3
from autocorrect import Speller
spell=Speller(lang='en')
spell('engilish')
spell('goodi')
#spell=Speller(lang='')
#spell('आह')

######################
import nltk
nltk.download('punkt')
from nltk import word_tokenize
sentence3="ntural languge processsin delds wiht teh aart of extracing settinments"
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word)for word in sentence3])
print(corrected_sentence)
######################

#STEMMING=>convert derived word into original form
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("Jumping")
stemmer.stem("standard")

#####################
#LEMATIZER=>
#lematizer looks into dict words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programmed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")

################
#chunking(shallow parsing) Identified named entities
nltk.download("maxent_ne_chunker")
nltk.download("words")
sentence4="we are learning NLP in python in sanjivani"
##first we will tokenize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
#O/P=>[Tree('NE', [('NLP', 'NNP')])]

##########################
#SENTENCE TOKENIZATION
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in python.Deliverd by sanjivaniAI. Do you know where is it located? It is in kopergaon")
sent
#O/P=>['we are learning NLP in python.Deliverd by sanjivaniAI.',
 #'Do you know where is it located?',
 #'It is in kopergaon']
 
#########################
## he went to bank and checked account it was almost 
#looking this he went to river bank and was crying

#LESK
from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
#O/P=>Synset('savings_bank.n.02')


#####################
sentence2="it is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
#O/P=>Synset('bank.v.07')

############# 14-06-2024 ################

"""removing special characters

special characters ,as you know ,
are non-alphanumeric characters.
These characters are most often found in comments,
references,currency numbers etc
These characters add no value to text-understanding
and induce noice into algorithms 
for that regex package is used"""

"""
go on google and search for-> regex101.com
then ->choose the python language->choose/select/write the sentence
in the test string->select the pattern and write in that pattern column
->u will see the description

"""

##########################
# To import regex

import re
chat1='Hello,I am having an issue with my order # 412889912 '
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern, chat1)
matches
#Out[11]: ['412889912']

#################################
chat2='Hello,I am having an issue with my order 412889912 '
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern, chat2)
matches
#Out[12]: ['412889912']

##################################
chat3='my order 412889912 is having an issue,I was charged'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern, chat3)
matches
#Out[13]: ['412889912']

#####################################
#it will be difficult to remember this all so will define in the function
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)',chat1)
#Out[10]: '412889912'

###########18/06/2024###########


import re
chat1="Hello I am having an issue with my order #83628746"
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)',chat1)
#Output: '83628746'
###############

chat1='you ask lot of qustions 1234456,abc@xyz.com'
chat2='here it is:(123)-8912,abc@xyz.com'
chat3='yes,phone:12345678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
#O/P=> 'abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
#O/P=> 'abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
#O/P=> 'abc@xyz.com'


#################
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)
#O/P: ('1234567891', '')

#################
#\(age(\d+)/)
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''
get_pattern_match(r'age (\d+)',text)
#O/P:52
get_pattern_match(r'Born(.*)',text).strip()
#O/P: 'Elon Reeve Musk'
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
#O/P:'June 28, 1971'
get_pattern_match(r'\(age.*\n(.*)',text)
#O/P: 'Pretoria, Transvaal, South Africa'

#############19/06/2024################

import re
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''
get_pattern_match(r'age (\d+)',text)
#O/P:52
get_pattern_match(r'Born(.*)',text).strip()
#O/P: 'Elon Reeve Musk'
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
#O/P:'June 28, 1971'
get_pattern_match(r'\(age.*\n(.*)',text)
#O/P: 'Pretoria, Transvaal, South Africa'

def extract_personal_information(text):
    age= get_pattern_match(r'age (\d+)',text)
    name= get_pattern_match(r'Born(.*)',text).strip()
    birth_date= get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
    birth_place= get_pattern_match(r'\(age.*\n(.*)',text)
    #mulltiple variables can be extract from paragraph(multiline text) in python
    return{
        'age': int(age),
        'name': name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
        }
extract_personal_information(text)
#Out[37]: 
#{'age': 52,
 #'name': 'Elon Reeve Musk',
 #'birth_date': 'June 28, 1971',
 #'birth_place': 'Pretoria, Transvaal, South Africa'}

#############################


text='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
import re
def extract_personal_information(text):
    age=get_pattern_match(r'age (\d+)',text)
    full_name=get_pattern_match(r'Born(.*)',text).strip()
    birth_date=get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
    birth_place=get_pattern_match(r'\(age.*\n(.*)',text)
    #mulltiple variables can be used in python
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)

##########################

from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader
#creating a pdf reader object
reader=PdfReader('C:/1-python/kopargaon-part-1.pdf') 
#printing number of pages in pdf file
print(len(reader.pages))
#getting specific page from the pdf
page=reader.pages[2]
page 

text=page.extract_text()
print(text)
#####################

reader2=PdfReader('C:/1-python/matrix_basics.pdf')
print(len(reader2.pages))
page=reader2.pages[2]
page
#display data of 2nd page
#extracting text from page
text=page.extract_text()
print(text)




##############20/06/2024###############

import re
sentence5="sharat twitted, Witnessing 68th republic day India from Rajpath,\new Delhi,Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+','',sentence5).split()
sentence5
'''
['sharat',
 'twitted',
 'Witnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 'ew',
 'DelhiMesmorizing',
 'performance',
 'by',
 'Indian',
 'Army']
'''

'''
re.sub(r'([^\s\w]|_)+','',some_string()
       will replace
       
'''
###################

#extracting n-grams
#n-grams are extracting using 3 techniques
#1.custom defined function
#2.NLTK
#3.Text Blob
#################
#n-grams-> extracting 1/2/3/4 words from the sentence
#extracting n_grams using customed defined fnction
import re
def n_gram_extractor(input_str,n):
    tokens=re.sub(r'([^\s\w]|_)+','',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
n_gram_extractor("The cute little boy is playing with kitten",2)       
'''['The', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'is']
['is', 'playing']
['playing', 'with']
['with', 'kitten']
''' 
n_gram_extractor("The cute little boy is playing with kitten",3)
'''['The', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'is']
['boy', 'is', 'playing']
['is', 'playing', 'with']
['playing', 'with', 'kitten']
'''
####################

#1.Extract all twitter handles from following text.Twitter handle
text='''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern='https://twitter.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)

#####################

#2.Extract Concentration Risk Types.It will be a text app
text='''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.

'''
pattern='Concentration of Risk:([^\n]*)'
re.findall(pattern,text)
#O/P->[' Credit Risk', ' Supply Risk']

#3.Companies in Europe reports their financial numbers of semi annual
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))'#?:match this and a|b
re.findall(pattern,text)
#O/P-> ['2021 Q1', '2021 S1']

##############################
import re
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches
#O/P->['9991116666', '(999)-333-7777']

###############################

text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern='Note \d - ([^\n]*)'
re.findall(pattern,text)
#O/P->['Overview', 'Summary of Significant Accounting Policies']

##################################

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
re.findall(pattern,text)
#O/P-> ['FY2021 Q1', 'FY2020 Q4']

##################################

text = '''
Tesla's gross cost of operating lease vehicles in fy2021 Q1 was $4.85 billion. 
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text,flags=re.IGNORECASE)
matches

############21/06/2024##############

#HW->creating df using list

from nltk import ngrams
#extraction n-grams with nltk
list(ngrams("The cute little boy is playing with kittens".split(),2))
#0/P->is in the form of list of tuples
'''
[('The', 'cute'),
 ('cute', 'little'),
 ('little', 'boy'),
 ('boy', 'is'),
 ('is', 'playing'),
 ('playing', 'with'),
 ('with', 'kittens')]
'''
list(ngrams("The cute little boy is playing with kittens".split(),3))
'''
[('The', 'cute', 'little'),
 ('cute', 'little', 'boy'),
 ('little', 'boy', 'is'),
 ('boy', 'is', 'playing'),
 ('is', 'playing', 'with'),
 ('playing', 'with', 'kittens')]
'''
from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kittens")
blob.ngrams(n=2)
'''
[WordList(['The', 'cute']),
 WordList(['cute', 'little']),
 WordList(['little', 'boy']),
 WordList(['boy', 'is']),
 WordList(['is', 'playing']),
 WordList(['playing', 'with']),
 WordList(['with', 'kittens'])]
'''
blob.ngrams(n=3)
'''
[WordList(['The', 'cute', 'little']),
 WordList(['cute', 'little', 'boy']),
 WordList(['little', 'boy', 'is']),
 WordList(['boy', 'is', 'playing']),
 WordList(['is', 'playing', 'with']),
 WordList(['playing', 'with', 'kittens'])]
'''
#tokenisation using keras
sentence5="sharat twitted, Witnessing 68th republic day India from Rajpath,\new Delhi,Mesmorizing performance by Indian Army!"
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)

#######################

#tokenisation using textblob
from textblob import TextBlob
sentence5="sharat twitted, Witnessing 68th republic day India from Rajpath,\new Delhi,Mesmorizing performance by Indian Army!"
blob=TextBlob(sentence5)
blob.words
#O/P->WordList(['sharat', 'twitted', 'Witnessing', '68th', 
#'republic', 'day', 'India', 'from', 'Rajpath', 'ew', 'Delhi', 
#'Mesmorizing', 'performance', 'by', 'Indian', 'Army'])

#######################

#text tokeniaer
from  nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)
#O/P->
'''
['sharat',
 'twitted',
 ',',
 'Witnessing',
 '68th',
 'republic',
 'day',
 'India',
 'from',
 'Rajpath',
 ',',
 'ew',
 'Delhi',
 ',',
 'Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army',
 '!']
'''

########################
#Multi_world_experience
from nltk.tokenize import MWETokenizer
'''
multi-word tokenizers are essential for tasks where the meaning of text heavily 
depends on the interpretation of phrases as wholes rather than
as sums of individual words.For  instance, in sentiment analysis, recognizing "not good"
as a single negative sentimemt unit rather than as "not" and "good" separately can
significantly affect the outcome
'''
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
#O/P->
'''
['sharat',
 'twitted,',
 'Witnessing',
 '68th',
 'republic_day',
 'India',
 'from',
 'Rajpath,',
 'ew',
 'Delhi,Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army!']
'''
mwe_tokenizer.tokenize(sentence5.replace('!','@').split())
#O/P->
'''
['sharat',
 'twitted,',
 'Witnessing',
 '68th',
 'republic_day',
 'India',
 'from',
 'Rajpath,',
 'ew',
 'Delhi,Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army']

'''
######################
#parse matrix






