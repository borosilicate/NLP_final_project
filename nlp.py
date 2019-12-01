import gensim
import spacy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_lg")
#model=gensim.models.Word2Vec('The monkey runs fast. The eagle is a horse.')

aar=np.load('data/agency_rank_ar.npy')
car=np.load('data/communion_rank_ar.npy')
score_dic={}
words=''
for k in aar[:]:
    words+=str(k[1])+' '
    score_dic[str(k[1])]=k[0]
for k in car[:]:
    words+=str(k[1])+' '
    score_dic[str(k[1])]=k[0]
model=nlp(words)
z=np.zeros([len(model)+1,len(model)+1])
harvest=z
for i,t1 in enumerate(model):
    for j,t2 in enumerate(model):
        z[i,j]+=t1.similarity(t2)
    print('still running',len(model)-i)

fig, ax = plt.subplots()
im = ax.imshow(harvest)

# We want to show all ticks...
print('starting axis')
ax.set_xticks(np.arange(len(model)))
ax.set_yticks(np.arange(len(model)))
# ... and label them with the respective list entries
ax.set_xticklabels(words.split())
ax.set_yticklabels(words.split())
print('done with axis')
# Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
#for i in range(len(model)):
#    for j in range(len(model)):
#        text = ax.text(j, i, harvest[i, j],
#                       ha="center", va="center", color="w")
#        print('setting text',len(model)-i)

ax.set_title("Agency vs Communion Similarity")
fig.tight_layout()
print('plt.show')
plt.show()
#plt.matshow(z)
#plt.show()

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
