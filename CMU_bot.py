### import package for img crawler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import urllib
from bs4 import BeautifulSoup
import requests

### import module
from utils.utils import get_credentials


# vist the aim url 
# driver = webdriver.Chrome(r'C:\Users\GTW_User\Desktop\CMU_bot\chromedriver-win32\chromedriver.exe')    
# driver.get("https://ceep2.tmu.edu.tw/")

## login
# input accountid and password
account, password = get_credentials()
# account = 223060
# password = 9537
print(account)
print(password)
# username_elem = driver.find_element_by_xpath('//*[@id="form3"]') # id : form3
# password_elem = driver.find_element_by_xpath('//*[@id="form2"]') # id : form2
# username_elem.send_keys(str(account))  
# password_elem.send_keys(str(password))  
# # press the login button
# login_button = driver.find_element_by_xpath('//*[@id="form"]/div[4]/button')
# login_button.click()
