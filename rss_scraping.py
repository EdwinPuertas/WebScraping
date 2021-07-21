from scraping import Scraping

urls = ['https://www.eltiempo.com/rss/vida_ciencia.xml',
        'https://www.eltiempo.com/rss/colombia.xml',
        'https://www.eltiempo.com/rss/colombia.xml',
        'https://www.eltiempo.com/rss/vida_viajar.xml',
        'https://www.eltiempo.com/rss/tecnosfera.xml',
        'https://www.eltiempo.com/rss/tecnosfera_dispositivos.xml']

sc = Scraping()
articles = list()
for url in urls:
    articles.extend(sc.rss(url=url))

for art in articles:
    print(art)
