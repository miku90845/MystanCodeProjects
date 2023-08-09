"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # ----- Write your code below this line ----- #
        tags = soup.find_all('tr')
        total_boy = 0
        total_girl = 0
        # 略過第一行的<tbody>
        for tag in tags[1:]:
            tds = tag.find_all('td')
            # 確保tds長度夠
            if len(tds) >= 3:
                count_boy = tds[2].text.replace(',', '')
                count_girl = tds[4].text.replace(',', '')
                total_boy += int(count_boy)
                total_girl += int(count_girl)
        print(f'Male Number: {total_boy}')
        print(f'Female Number: {total_girl}')


if __name__ == '__main__':
    main()
