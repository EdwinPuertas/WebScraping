import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


class Scraping(object):
    """ Class used scraping resources"""

    def rss(self, url: str = '') -> list:
        article_list = []
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, features='xml')
            articles = soup.findAll('item')
            for a in articles:
                title = a.find('title').text
                link = a.find('link').text
                description = a.find('description').text
                published = a.find('pubDate').text
                article = {
                    'title': title,
                    'link': link,
                    'description': description,
                    'published': published,
                    'items': soup.findAll('item')
                    }
                article_list.append(article)
            return article_list
        except Exception as e:
            print('The scraping rss job failed. {0}'.format(e))
            return list()

    def web(self, url: str) -> list:
        try:
            data = []
            # webdriver = Chrome(ChromeDriverManager().install())
            webdriver = r"C:/Users/Edwin Puertas/.wdm/drivers/chromedriver/win32/86.0.4240.22/chromedriver.exe"
            driver = Chrome(webdriver)

            parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
            resp = urllib.request.urlopen(url)
            soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
            links = list()
            for row in soup.find_all('a', href=True):
                path = str(row['href'])
                if path.find('/') == 0 and path.count('/') >= 1:
                    if (url + path) not in links:
                        links.append(url + path)

            for page in links:
                driver.get(page)
                if str(driver.title) != 'Error404':
                    title = driver.title
                    text = driver.find_element_by_tag_name("body").text
                    if text != '':
                        # print(driver.page_source)
                        row = [title, text]
                        print(row)
                        data.append(row)
            driver.close()
            return data
        except Exception as e:
            print('The scraping web job failed. {0}'.format(e))
            return list()