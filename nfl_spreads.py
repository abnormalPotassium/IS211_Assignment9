from bs4 import BeautifulSoup
from urllib import request
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('--teamOne', nargs='?')
parse.add_argument('--teamTwo', nargs='?')
args = parse.parse_args()

teamOne = str(args.teamOne)
teamTwo = str(args.teamTwo)

url = 'http://www.footballlocks.com/nfl_point_spreads.shtml'
page = request.urlopen(url)
soup = BeautifulSoup(page.read(),features='html.parser')

point_spreads_raw = soup.find_all('table', attrs = {'cols': '4', 'width': '580'})
point_spreads_cooking1 = [table.find_all('tr')[1:] for table in point_spreads_raw]
point_spreads_cooking2 = [row for list in point_spreads_cooking1 for row in list]

point_spreads = []
point_spreads_dict = {}
for row in point_spreads_cooking2:
    game = row.find_all('td')
    date = game[0].contents[0]
    favorite = game[1].contents[0]
    spread = game[2].contents[0]
    underdog = game[3].contents[0]

    if favorite.startswith('At '):
        favorite = favorite[len('At '):]
        point_spreads.append(f'On {date}, the favorites to win are {favorite} at their home field against the underdog {underdog} with a spread of {spread}.')

    elif underdog.startswith('At '):
        underdog = underdog[len('At '):]
        point_spreads.append(f'On {date}, the favorites to win are {favorite} against the underdog {underdog} at their home field with a spread of {spread}.')

    else:
        point_spreads.append(f'On {date}, the favorites to win are {favorite} against the underdog {underdog} with a spread of {spread}.')

    point_spreads_dict[favorite,underdog] = [date,spread]

def main():
    if teamOne and teamTwo:
        for a,b in point_spreads_dict.keys():
            if all(x in [a,b] for x in [teamOne,teamTwo]):
                print(f'On {point_spreads_dict[a,b][0]}, the favorites to win are {a} against the underdog {b} with a spread of {point_spreads_dict[a,b][1]}.')
                raise SystemExit
    for game in point_spreads:
        print(game)

if __name__ == "__main__":
    main()