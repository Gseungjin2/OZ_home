import requests
from bs4 import BeautifulSoup

keywrod = input("검색할 상품 : ")
baes_url = f"https://coupang.com/np/search?component=&q={keywrod}" # 쿠팡 뒤에 붙어있는건 쿼리 스트링 지워도 뭅아

header_user = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36" }
cookie = {"sorry" : "cookie"}

req = requests.get(baes_url, headers=header_user, cookies=cookie, timeout= 3)

html = req.text
soup = BeautifulSoup(html, "html.parser")


items = soup.select("[class=search-product  ]")

for rank, item in enumerate(items, 1):
    name = item.select_one(".name").text
    price = item.select_one(".price-value").text
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")
    roket = item.select_one(".badge.rocket")

    print(f"[{rank}]위")
    print(f"제품명 : {name}")
    print(f"{price}원")
    # print(f"이미지 URL : {img_src}")
    if roket:
        print("로켓 배송 가능")
    else:
        print("로켓 배송 불가능")
    print(f"쿠팡 링크 : https://www.coupang.com{link}")
    if img_src.get("data-img-src"):
        img_url = f"https:{img_src.get('data-img-src')}"
    else:
        img_url = f"https:{img_src.get('src')}"

    print(f"이미지 URL :  {img_url}")
    print()

    img_req = requests.get(img_url)
    with open(f"img/{rank}.jpg", "wb") as f:
        f.write(img_req.content)


