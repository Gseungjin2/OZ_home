from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.img-logo').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.nav_item:nth-of-type(3) > a').click()
time.sleep(1)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(1)

driver.find_element(By.XPATH, "//button[@onclick='hasMore2();']").click() #onclick이 hasMore2() 인걸 클릭하게 해줘

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")

wrap = soup.select('.list_item')

for i in wrap:
    title = i.select('.title.ellipsis')
    singer = i.select('.name.ellipsis')
    rank = i.select('.ranking_num')

    for r, t, s in zip(rank, title, singer):
        print(r.text.strip())
        print(f"제목: {t.text.strip()}")
        print(f"가수: {s.text.strip()}")
        print('')

driver.quit()