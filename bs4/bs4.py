import requests, bs4
from BeautifulSoup import *
res = requests.get('http://www.cricbuzz.com/cricket-match/live-scores')
res.raise_for_status()
score_text = bs4.BeautifulSoup(res.text)
score=score_text.select('span')
print(type(score))
