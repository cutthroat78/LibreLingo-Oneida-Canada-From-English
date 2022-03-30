# https://www.geeksforgeeks.org/python-web-scraping-tutorial/
# https://stackoverflow.com/questions/59539194/how-to-download-all-mp3-url-as-mp3-from-a-webpage-using-python3

import requests
from bs4 import BeautifulSoup
 
link = input("Webpage Link: ")
skill = input("Skill Name: ")

# Making a GET request
r = requests.get(link)
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Find and sort files into csv format
oneida_word = soup.find_all('p', class_= 'oneida')
english_word = soup.find_all('p', class_= 'english') 
for one,eng in zip(oneida_word,english_word):
    print (str(one.get_text()) + ","  + str(eng.get_text()))

# Download audio files
for tag in soup.find_all('a', class_= 'action primary'):
    link = tag.get('href')
    r = requests.get(link)
    filename = tag['href'][tag['href'].rfind("/")+1:]
    with open(filename, 'wb') as f:
        f.write(r.content)
