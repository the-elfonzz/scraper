import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


URL = 'https://apnews.com/apf-topnews'


class Agent:
    def __init__(self)->None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
        self.driver.get(URL)

    def get_articles(self)->None:
        article_titles, links = self.get_article_names()
        self.print_articles(links, article_titles)

    def get_article_names(self)->None:
        articles = self.driver.find_elements(By.XPATH, "//a[h1]")
        article_titles = [elem.text for elem in articles]
        links = [elem.get_attribute('href') for elem in articles]
        return article_titles , links

    def print_articles(self, links:list, article_titles:list)->None:
        art_no = 0
        for link in links:
            try:
                self.driver.get(link)
                article_title = article_titles[art_no]
                article_body, = self.driver.find_elements(By.XPATH, "//div[@class='Article'] | //article[p] | //article[div]")
                art_no +=1
                print(article_title, article_body.text)
            except:
                print('pass')
                pass #There is an eror on parsing the third element's body and I don't know why so I allow it
