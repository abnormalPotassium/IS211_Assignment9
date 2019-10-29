from bs4 import BeautifulSoup
from urllib import request
import csv

url = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns'
page = request.urlopen(url)
soup = BeautifulSoup(page.read(),features='html.parser')

top20_raw = soup.find_all('tr', attrs = {'class' : ['row1','row2']})[:20]
top20 = []

for i, row in enumerate(top20_raw):
    player = row.contents[0].contents[0].contents[0]
    position = row.contents[1].contents[0]
    team = row.contents[2].contents[0].contents[0]
    touchdowns = row.contents[6].contents[0]
    top20.append(f'{player} is the top #{i+1} league leader in touchdowns! He has {touchdowns} touchdowns and plays on {team} as an {position}.')

def main():
    for player in top20:
        print(player)

if __name__ == "__main__":
    main()
