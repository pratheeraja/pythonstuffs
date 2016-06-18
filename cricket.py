import requests, bs4
from BeautifulSoup import *

res = requests.get('http://www.cricbuzz.com/cricket-match/live-scores')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
mydivs = soup.findAll("div", { "class" : "cb-lv-scrs-col cb-font-12 text-black" })
le=len(mydivs)
result=""
for l in range(0,le-1):
    result += str(mydivs[l].getText())+'\n'
print(result)

