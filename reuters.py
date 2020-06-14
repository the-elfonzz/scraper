from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse


URL = 'https://www.reuters.com/'


class Agent:
    def __init__(self)->None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        self.driver.get(URL)
        self.driver.find_element_by_id('_evidon-banner-acceptbutton').click()
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def get_articles(self)->None:
        links = self.get_article_names()
        self.print_articles(links)

    def get_article_names(self)->None:
        articles = driver.find_elements(By.XPATH, "//h2[@class='story-title']/a | //a[h3[contains(@class,'story')]] \
                                                   | //a[div[@class='story-headline']] | //h3[@class='story-title']/a")
        links = [elem.get_attribute('href') for elem in articles]
        print(links)
        return links

    def print_articles(self, links:list)->None:
        for link in links:
            driver.get(link)
            article_title, = driver.find_elements(By.XPATH, "//h1[@class='ArticleHeader_headline']")
            article_body, = driver.find_elements(By.XPATH, "//div[@class='StandardArticleBody_body']")
            print(article_title.text, article_body.text)