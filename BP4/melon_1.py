import requests
from bs4 import BeautifulSoup


header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://naver.com"

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
url = "https://www.melon.com/chart/index.htm"

req = requests.get(url, headers=header_user)  
html = req.text

soup = BeautifulSoup(html, "html.parser")

ranking= soup.select(".wrap.t_center")
title = soup.select(".ellipsis.rank01")
singer = soup.select(".ellipsis.rank02")

album = soup.select(".wrap")

for i in zip(ranking, title, singer, album):
    print(f"순위 : {i[0].text}")
    print(f"제목 : {i[1].text}")
    print(f"가수 : {i[2].text}")
    print(f"앨범 : {i[3].text}")
    print()



#[순위]
#제목 : 정보
#가수 : 정보
#앨범 : 정보


