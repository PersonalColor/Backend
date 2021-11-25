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

codi_data = {}

driver = webdriver.Chrome()

color_list = ['흰색', '검정색', '회색', '갈색', '베이지색', '녹색', '파란색', '데님', '보라색', '노란색', '분홍색', '빨간색', '주황색', '은색', '금색', '기타']

for index in range(1, 17):
    print(codi_data)
    driver.get(f'https://magazine.musinsa.com/index.php?m=street&_y=2021&_mon=11%2C10%2C09&color={index}')
    codi_data[color_list[index - 1]] = []
    for index in range(0, 30):
        try:
            driver.find_elements(By.CLASS_NAME, 'articleImg')[index].click()

            link = driver.current_url
            res = requests.get(link, headers=headers)
            res.raise_for_status()
            soup = BeautifulSoup(res.text, "html.parser")

            listItem = soup.select_one(".styleItem-box")
            a = listItem.select('a')
            itemname = listItem.select('p')
            
            tbody = soup.select_one('tbody')

            span = tbody.select('span')
            name = str(span[1].text)
            day = str(span[4].text)
            area = str(span[9].text)

            detail = []

            url = driver.find_elements(By.CLASS_NAME, 'lbox')[0].get_attribute('href')

            cnt = 0
            for k in range(len(a)):
                if(re.search('title(.+?)"', str(a[k]))):
                    cnt = cnt + 1
            
            fir = -5
            for i in range(cnt):
                deitem = re.search('href="(.+?)"',str(a[fir+5]))
                if deitem:
                    deitem = deitem.group(1)
                    detail.append({
                        "title": itemname[i].text.strip(),
                        "image": "https:" + deitem
                    })
                fir+=5

            codi_data[color_list[index]].append({
                "name": name,
                "filmingDate": day,
                "area": area,
                "image": url,
                "detail": detail
            })

            driver.back()
        except:
            break

print(codi_data)

f = open("../../data/style/style.json", 'w')
f.write(json.dumps(codi_data))
f.close()