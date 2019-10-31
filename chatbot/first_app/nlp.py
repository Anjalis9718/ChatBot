#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 00:11:28 2019

@author: anjali
"""

import numpy as np
import tensorflow as tf
import re
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

import random

import nltk
from nltk.stem import WordNetLemmatizer



query = open('AirIndia.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
while("" in query) :
    query.remove("")

questions=[]
answers=[]
for line in query:
    _line = line.split('+++$+++')

    answers.append(_line[1])
    questions.append(_line[0])

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):

    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]", "", text)
    return text

from nltk import word_tokenize

from nltk.corpus import stopwords



def stopwords_remo(text1):
    text1 = ' '.join([word for word in text1.split() if word not in stopwords.words("english")])
    return text1;


filtered_questions=[]
for question in questions:
    filtered_questions.append(stopwords_remo(question))




# Cleaning the answers


def response(user_response):
    robo_response=''
    filtered_questions.append(user_response)

    TfidfVec = TfidfVectorizer()
    tfidf = TfidfVec.fit_transform(filtered_questions)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+answers[idx]
        return robo_response

def reply(inputx):
    user_response=inputx.lower()
    if(greeting(user_response)!=None):
        text3="ROBO: "+greeting(user_response)
    else:

        text3=response(user_response)
        filtered_questions.remove(user_response)



    return text3
