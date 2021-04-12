""" File to define get_soup() helper method """

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def initiate_webdriver():
    """ Returns a headless chromium web driver """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def get_page_source(link, driver):
    """ Return the page source of a website using a webdriver """
    driver.get(link)
    content = driver.page_source
    return content


def get_soup(link, driver):
    """ Return the BS4 soup for the given page source """
    page_source = get_page_source(link, driver)
    soup = BeautifulSoup(page_source, features='html.parser')
    return soup
