from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"

options = Options()
options.add_argument(f"user-agent={header_user}")
options.add_argument(f"User-Agent={header_user}")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)



url = "https://kream.co.kr/"
driver.get(url)
time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, ".search_btn_box").click()
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
# time.sleep(1)

# driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
# time.sleep(1)

# for i in range(30):
#     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
#     time.sleep(0.5)

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# #item_inner
# items = soup.select(".item_inner")

# product_list = []

# for i in items:
#     product_name = i.select_one(".translated_name").text
#     if "후드" in product_name:
#         category = "상의"
#         product_brand = i.select_one(".product_info_brand.brand").text  # "슈프림" 이라고 쓸수도 잇음 # 확장성 쓸거면 현재처럼 작성
#         product_name_hood = i.select_one(".translated_name").text
#         product_price = i.select_one(".amount").text

#         print(category, product_brand, product_name_hood, product_price)

# driver.quit() #웹 드라이버 종료 및 브라우저 닫기