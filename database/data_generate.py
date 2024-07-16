import mysql.connector
from faker import Faker # from 페이커 라는 모듈에서 불러오겠다
import random # 파이썬 기본 모듈

# (1) MYSQL 연결 설정 
db_connention = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Penta12./',
    database = 'testdatabase'
)

# (2) MYSQL 연결
cursor = db_connention.cursor()
faker = Faker()

# users 데이터 생성

for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)
    
    cursor.execute(sql, values)

cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]


# 100개의 주문 덤이 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)

        cursor.execute(sql, values)
    except:
        print("오류 발생")
        pass


db_connention.commit()
cursor.close()
db_connention.close()
    # print(sql)