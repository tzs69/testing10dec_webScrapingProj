
from pip._vendor import requests
from bs4 import BeautifulSoup
import re

url = "xxx" #enter tapology global top 50 fighters url here (any weight class)
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

weightClassList = soup.find('div', class_ = "pageHeading withSharing").find('h1').text.split(" ")
if len(weightClassList) == 9: 
    weightClass = weightClassList[4] + " " + weightClassList[5]
else: 
    weightClass = weightClassList[4]

top50global = soup.find_all('li', class_ = "rankingItemsItem")

total_Wins = 0
total_Losses = 0
total_Draws = 0
total_NoContests = 0

for fighter in top50global:
    winloss = fighter.find('h1', class_ = "right")
    record = re.split("-|, | ", winloss.text)
    total_Wins += int(record[0])
    total_Losses += int(record[1])
    total_Draws += int(record[2])
    if len(record) != 3:
        total_NoContests += int(record[3])

print("The combined record of the top 50 %s globally is %i-%i-%i(Win-Loss-Draw) with %i No Contests" % (weightClass, total_Wins, total_Losses, total_Draws, total_NoContests))



