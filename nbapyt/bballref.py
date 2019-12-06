# Scrape Basketball-Reference webpage
from config import key
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time
import sys
import requests

# URL = "https://www.basketball-reference.com/players/j/jamesle01.html"
# r = requests.get(URL)
#
# soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

#################
# OPEN BBAL REF #

# get query
# playerQuery = input("Enter Player name: ")

while 1:
    try:
        while True:
            playerQuery = input("Enter Player name: ")
            # open webdriver
            driver = webdriver.Chrome('./chromedriver')

            # open bbal ref webpage
            driver.get(key['url'])

            # search player
            driver.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/input[2]').send_keys(playerQuery)

            # click search
            driver.find_element_by_xpath('//*[@id="header"]/div[3]/form/input[1]').click()
            time.sleep(2)

            element = driver.find_element_by_xpath('/html/head/link[11]')
            href = element.get_attribute('href')
            href = href[:45]

            # # if search = 0
            # element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/p[1]/strong')
            # hits = element.get_attribute('hits')
            # print(hits)

            if href == 'https://www.basketball-reference.com/players/':
                # player page alraedy opened after Query
                # do nothing
                pass
            else:
                # click first player in query
                # //*[@id="players"]/div[1]/div[1]/a
                try:
                    elem = driver.find_element_by_xpath('//*[@id="players"]/div[1]/div[1]/a').click()
                except NoSuchElementException:  #spelling error making this code not work as expected
                    driver.find_element_by_xpath('//*[@id="players"]/div[1]/div[1]/strong/a').click()
    except KeyboardInterrupt:
        pass

# # open webdriver
# driver = webdriver.Chrome('./chromedriver')
#
# # open bbal ref webpage
# driver.get(key['url'])
#
# # search player
# driver.find_element_by_xpath('//*[@id="header"]/div[3]/form/div/div/input[2]').send_keys(playerQuery)
#
# # click search
# driver.find_element_by_xpath('//*[@id="header"]/div[3]/form/input[1]').click()
# time.sleep(2)
#
# element = driver.find_element_by_xpath('/html/head/link[11]')
# href = element.get_attribute('href')
# href = href[:45]
#
# # if search = 0
# element = driver.find_element_by_xpath('//*[@id="content"]/div[1]/p[1]/strong')
# hits = element.get_attribute('hits')
# print(hits)
#
# if href == 'https://www.basketball-reference.com/players/':
#     # player page alraedy opened after Query
#     # do nothing
#     pass
# else:
#     # click first player in query
#     # //*[@id="players"]/div[1]/div[1]/a
#     try:
#         elem = driver.find_element_by_xpath('//*[@id="players"]/div[1]/div[1]/a').click()
#     except NoSuchElementException:  #spelling error making this code not work as expected
#         driver.find_element_by_xpath('//*[@id="players"]/div[1]/div[1]/strong/a').click()

# OPEN BBAL REF DONE #
######################



###############
# SCRAPE DATA #

#






# DATA SCRAPPED #
#################

