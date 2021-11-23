from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re
import time
import json

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'    
}

codi_data = []

driver = webdriver.Chrome()

color = '베이지'

driver.get(f'https://magazine.musinsa.com/index.php?m=street&style=002&ordw=hit&_y=2021&color=5&swh=&stx={color}')

images = driver.find_elements(By.CLASS_NAME, 'articleImg')

for index in range(1, len(images) + 1):
    driver.find_elements(By.CLASS_NAME, 'articleImg')[index].click()
    driver.back()


f = open("style.json", 'w')
f.write(json.dumps(codi_data))
f.close()