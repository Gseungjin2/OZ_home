import requests
from bs4 import BeautifulSoup

url = "https://naver.com"

req = requests.get(url) #.get(htts://naver.com)
# print(req)

html = req.text 
# print(html)

# 트리구조로 만드는게 파싱
soup = BeautifulSoup(html, "html.parser") # 함수나 클래스형태다
# print(soup)

query = soup.select_one(".search_input_box") # 크롤링에서 . 은 클래를 뜻함
print(query)