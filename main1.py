from bs4 import BeautifulSoup
import nltk
import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer


tokenizer = RegexpTokenizer(r'\w+')
column_titles = ['student name', 'response']
answers = []

with open('home.html','r') as html_file:
    content = html_file.read()
    soup= BeautifulSoup(content,'lxml')
    #print(soup.prettify())
    polls_html_tags = soup.find_all('pre')
    names = soup.find_all('p')
    for i in range(len(names)):
        #filters out punctuations and separates a sentence into words
        #filtered_answer = tokenizer.tokenize(polls_html_tags[i].text)
        answers.append([names[i].text,polls_html_tags[i].text.split()])
    # for name in names:
    #     print(name.text)
    # for poll in polls_html_tags:
    #     answers.append(poll.text)

df=pd.DataFrame(columns=column_titles, data = answers)

#print(answers[0][1])
#def poll_grader(poll,keywords )

keywords1 = ['0.7/0.5']
keywords2 = ['']
n_keywords1 = ['%']



class Poll:
    def __init__(self, name, answer):
        self.name = name
        self.answer = answer

class poll_grader:
    def __init__(self, polls):
        self.polls = polls

    def calculation_check(answers):
        for i in range(len(answers)):
            for keyword in keywords1:
                if keyword in answers[i][1]:
                    print(answers[i][0]) 
df