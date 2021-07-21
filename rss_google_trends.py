from logic.scraping import Scraping

url = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=CO'
sc = Scraping()
articles = list()

resp = sc.rss(url=url)

for i in resp:
    print(i)

