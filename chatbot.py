#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#description:this is a 'smart' chat bot program


# In[1]:


pip install nltk 


# In[2]:


pip install newspaper3k


# In[2]:


#import the libraries
from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[3]:


#download the punkt(divide text into list of sentences 
#by using unsupervised algorithm) package
import nltk
nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize


# In[4]:


nltk.download('punkt',quiet=True)


# In[5]:


#get the article
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus = article.text


# In[5]:


#print the article text
print(corpus)


# In[6]:


#tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text)#a list of sentences


# In[7]:


#print the lisr of sentences
print(sentence_list)


# In[7]:


#a function to return a random greeting response to a user greeting
def greeting_response(text):
    text.lower()
    
    #bots greeting response
    bot_greetings = ['howdy','hi','hey','hello','hola']
    #users greeting
    user_greetings = ['hi','hey','hola','hello','greetings','wassup']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


# In[8]:


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


# In[9]:


#create the bot response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response=''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j+1
        if j>2:
            break
     
    if response_flag == 0:
        bot_response = bot_response+' '+"I apologize, I don't understand"
    sentence_list.remove(user_input)
    return bot_response


# In[ ]:


#start the chat
print('Doc Shivu: I am Doctor Shivu or Doc Shivu for short. I will answer our queries about Chronic Kidney Disease. If you want to exit,type bye.')
exit_list = ['exit','see you later','bye','quit','break']
while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Doc Shivu: Chat with you later !')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Shivu: '+greeting_response(user_input))
        else:
            print('Doc Shivu: '+bot_response(user_input))


# In[ ]:




