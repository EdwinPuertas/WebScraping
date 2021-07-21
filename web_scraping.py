from logic.scraping import Scraping

sc = Scraping()
articles = sc.web(url='https://www.eluniversal.com.co')
for art in articles:
    print(art)