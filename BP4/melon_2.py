import requests
from bs4 import BeautifulSoup

# User-Agent 설정
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

# Melon 차트 페이지 URL
url = "https://www.melon.com/chart/index.htm"

try:
    # 웹 페이지 요청
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 요청이 성공했는지 확인

    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 데이터 추출
    rankings = soup.select(".rank")
    titles = soup.select(".ellipsis.rank01")
    singers = soup.select(".ellipsis.rank02")
    albums = soup.select(".ellipsis.rank03")

    # 순위와 정보 출력
    for rank, title, singer, album in zip(rankings, titles, singers, albums):
        print(f"순위 : {rank.text.strip()}")
        print(f"제목 : {title.text.strip()}")
        print(f"가수 : {singer.text.strip()}")
        print(f"앨범 : {album.text.strip()}")
        print()

except requests.RequestException as e:
    print(f"웹 요청 중 오류 발생: {e}")
except Exception as e:
    print(f"알 수 없는 오류 발생: {e}")