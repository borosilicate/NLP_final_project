import gensim
import spacy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os
nlp = spacy.load("en_core_web_lg")
#model=gensim.models.Word2Vec('The monkey runs fast. The eagle is a horse.')

aar=np.load('data/agency_rank_ar.npy')
car=np.load('data/communion_rank_ar.npy')

'''
f=open('pulled/Letters_to_Madame_Hanska/Letters_during_1833.txt')
haskal=f.readline()

data_full=''
dic2=[]
for i in os.listdir('pulled'):
    for j in os.listdir('pulled/'+i):
        print(i,j)
        with open('pulled/'+i+'/'+j, 'r') as file:
            s=file.read().replace('\n', ' ').lower()
            s=s.strip(',').strip('\'s').strip('\\').replace('-',' ').strip(';')
            s=s.replace(';',' ')
            s=s.replace('\'s',' ')
            s=s.replace('-',' ')
            s=s.replace('.','')
            s=s.replace(',','')
            s=s.replace('?','')
            s=s.replace('!','')
            s=s.replace('\\','')
            dic2.append(s)



first=0
dictionary={}
for i in dic:
    for j in i.split():
        j=j.strip('!')
        j=j.strip('.')
        j=j.strip(',')
        j=j.strip('\'')
        if(first==0):
            if(j in dictionary):
                dictionary[j]+=1
            else:
                dictionary[j]=1
        else:
            if(j in dictionary):
                dictionary[j]+=1
    first+=1

for i in os.listdir('pulled'):
    for j in os.listdir('pulled/'+i):
        print(i,j)
f=open('agency_words.txt','r')
agency=f.readline()
agency=f.readlines()
with open('pulled/Letters_to_Madame_Hanska/Letters_during_1833.txt', 'r') as file:
    data = file.read().replace('\n', '')

doc=nlp(data)
doc.count_by
doc.count_by()
words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

# noun tokens that arent stop words or punctuations
nouns = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(5)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)
from collections import Counter
words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

# noun tokens that arent stop words or punctuations
nouns = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(5)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(5)
common_nouns
common_words
word_freq.most_common(10)
noun_freq.most_common(10)



'''
