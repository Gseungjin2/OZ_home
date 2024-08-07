import requests
from bs4 import BeautifulSoup

# 아래 유저 에이전트를 이용해서 초보 크롤러 걸러내기도함 그래서 유저 에전트 부분을 추가해서 아이피 막히느걸 미리 방어 해야함
header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://naver.com"

req = requests.get(url, header_user)     #.get(htts://naver.com)
# print(req.raise_for_status)
# print(req.request)


html = req.text 
# print(html)

# 트리구조로 만드는게 파싱
soup = BeautifulSoup(html, "html.parser") # 함수나 클래스형태다
# print(soup)

query = soup.select_one(".search_input_box") # 크롤링에서 . 은 클래를 뜻함
# print(query)

# 파이썬은 모든걸 html이든 머든 텍스트로 받기때문에 이걸 파싱을 이용해서 트리 구조로 정리 