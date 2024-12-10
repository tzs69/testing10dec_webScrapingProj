
from pip._vendor import requests
from bs4 import BeautifulSoup
import re

url = "xxx" #enter tapology top 50 fighters globally (specific weight class) link here
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

body_tag = soup.find('body', {'data-controller': "sidebar responsive grow-textarea", 'data-location': "rankings.show"})

general = body_tag.find('div', class_ = "contentWrap clearfix")
content = general.find('div', id = "content")

weightClassList = content.find('div', class_ = "pageHeading withSharing").find('h1').text.split(" ")
if len(weightClassList) == 9: 
    weightClass = weightClassList[4] + " " + weightClassList[5]
else: 
    weightClass = weightClassList[4]

top50global_list = content.find('ul', class_ = "rankingItemsList")
top50global = top50global_list.find_all('li', class_ = "rankingItemsItem")

total_Wins = 0
total_Losses = 0
total_NoContests = 0

for fighter in top50global:
    d0 = fighter.find('div', class_ = "rankingItemsItemRow name")
    d1 = d0.find('h1', class_ = "right")
    record = re.split("-|, ", d1.text)
    total_Wins += int(record[0])
    total_Losses += int(record[1])
    total_NoContests += int(record[2])

print("The total win-loss-NC ratio for the top 50 %s globally is %i-%i-%i" % (weightClass, total_Wins, total_Losses, total_NoContests))



