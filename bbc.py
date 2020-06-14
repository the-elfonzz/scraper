import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


URL = 'https://www.bbc.com/news'


class Agent:
    def __init__(self)->None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
        self.driver.get(URL)

    def get_articles(self)->None:
        links = self.get_article_names()
        self.print_articles(links)

    def get_article_names(self)->None:
        articles = self.driver.find_elements(By.XPATH, "//a[@class='gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor']")
        links = [elem.get_attribute('href') for elem in articles]
        return links

    def print_articles(self, links:list)->None:
        for link in links:
            self.driver.get(link)
            article_title, = self.driver.find_elements(By.XPATH, "//h1[@class='story-body__h1']")
            article_body, = self.driver.find_elements(By.XPATH, "//div[@class='story-body__inner']")
            print(article_title.text, article_body.text)

