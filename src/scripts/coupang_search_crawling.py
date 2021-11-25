import requests
from bs4 import BeautifulSoup
from urllib import parse
from datetime import datetime
import time
import json

category_list = ['상의', '하의', '악세서리', '신발', '화장품']
color_list = ['아이보리', '오렌지레드', '코랄핑크', '카멜', '머스타드', '오렌지', '버건디', '플럼', '블루그레이', '빨강', '블랙', '마젠타']

base_url = 'https://www.coupang.com/np/search?component=&q={}&channel=user'
cp_url = 'https://www.coupang.com/'

result_list = {
    "상의": {},
    "하의": {},
    "악세서리": {},
    "신발": {},
    "화장품": {}
}

for category in category_list:
    for color in color_list:
        result_list[category][color] = []

        params = {
            'q' : category,
        }

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'    
        }

        for page in range(1, 2):
            url = base_url.format(color + " " + category, page)
            res = requests.get(url, headers=headers)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, "html.parser")
                item_list = soup.select('ul#productList li')
                for item in item_list:
                    try:
                        item_name = item.select_one('div.name').text.strip() #상품이름
                        link = item.select_one('a').get('href')
                        link = parse.urljoin(cp_url, link) #상품 링크
                        price = item.select_one('strong.price-value').text.strip()
                        price = ''.join(price.split(',')) #가격

                        img_link = requests.get(link, headers=headers)
                        img_link.raise_for_status()
                        soup = BeautifulSoup(img_link.text, "html.parser") 
                        img_link = "http:"+ soup.select_one('#repImageContainer > img')['src'] #상품 세부 이미지

                        result_list[category][color].append({
                            "itemName": item_name,
                            "price": price,
                            "link": link,
                            "imgLink": img_link
                        })             
                    except:
                        pass


                   
json_result = json.dumps(result_list)
print(json_result, end="")