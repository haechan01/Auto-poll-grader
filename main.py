from bs4 import BeautifulSoup
import requests

html_text= requests.get('https://forum.minerva.edu/app/courses/2116/sections/8360/classes/61371/review').text
soup = BeautifulSoup(html_text,'lxml')
polls = soup.find_all('h3', class_="flex-auto")
print(polls)
