import requests, uuid, pprint, os, sys
from bs4 import BeautifulSoup

skill = sys.argv[1]
link = sys.argv[2]

# Making a GET request
r = requests.get(link)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

oneida_word = soup.find_all('p', class_= 'oneida')
english_word = soup.find_all('p', class_= 'english')
audio_links = []
for tag in soup.find_all('a', class_= 'action primary'):
    audio_links.append(tag.get('href'))

skill_head = "Skill:\n  Id: id\n  Name: skill"
skill_head = skill_head.replace("id",str(uuid.uuid4()))
skill_head = skill_head.replace("skill", "\"" + skill + "\"")

words_phrases = "\n\nNew words: []\n\nPhrases:\n"

file = open(skill + ".yaml", "a")
file.write(skill_head)
file.write(words_phrases)

if not os.path.exists("../../../audio/sort-oneidalangauge.ca/" + str(skill) + "/"):
    os.makedirs("../../../audio/sort-oneidalangauge.ca/" + str(skill) + "/")

for one,eng,url in zip(oneida_word,english_word,audio_links):
    phrase_translation = "  - Phrase: oneida\n  Translation: english\n\n"
    phrase_translation = phrase_translation.replace("oneida","\"" + str(one.get_text()) + "\"")
    phrase_translation = phrase_translation.replace("english","\"" + str(eng.get_text()) + "\"")
    file.write(phrase_translation)
    r = requests.get(url)
    filename = one.get_text() + ".mp3"
    with open(filename, 'wb') as f:
        f.write(r.content)
    os.rename("./" + str(one.get_text()) + ".mp3", "../../../audio/sort-oneidalangauge.ca/" + str(skill) + "/" + str(one.get_text()) + ".mp3")

file.close()
