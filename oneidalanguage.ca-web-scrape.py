# https://www.geeksforgeeks.org/python-web-scraping-tutorial/
# https://stackoverflow.com/questions/59539194/how-to-download-all-mp3-url-as-mp3-from-a-webpage-using-python3

# To-Do:
# Get all words and phrases from https://oneidalanguage.ca/learn-our-language/oneidalanguage-words-phrases/?t_id=0 pages and put in csv file and put that file in seperate git repo
# Ask for link and skill name
# Put data (with skill name) in yaml file (and generate unique ID for skill and put into file)
# Put audio files in desired folder structure (audio/$module_name/$skill_name/$oneida_word.mp3) and rename them to have the names of the Oneida words

import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://oneidalanguage.ca/learn-our-language/oneidalanguage-words-phrases/?t_id=137')
 
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
