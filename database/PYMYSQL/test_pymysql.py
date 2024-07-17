import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Penta12./',
    db='AirBnB',
)

quantity_sold = 10  # 예시 값
product_id = 1  # 예시 값
new_email = 'new_email@example.com'  # 예시 값
customer_id = 1  # 예시 값
order_id = 1  # 예시 값

try:
    with conn.cursor() as cursor:
        # 문제 1: 새로운 제품 추가
        sql_insert_product = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        cursor.execute(sql_insert_product, ('Python Book', 29.99, 50))

        # 문제 2: 고객 목록 조회
        sql_select_customers = "SELECT * FROM Customers"
        cursor.execute(sql_select_customers)
        for row in cursor.fetchall():
            print(row)

        # 문제 3: 제품 재고 업데이트
        sql_update_stock = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(sql_update_stock, (quantity_sold, product_id))

        # 문제 4: 고객별 총 주문 금액 계산
        sql_sum_orders = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
        cursor.execute(sql_sum_orders)
        for row in cursor.fetchall():
            print(row)

        # 문제 5: 고객 이메일 업데이트
        sql_update_email = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql_update_email, (new_email, customer_id))

        # 문제 6: 주문 취소
        sql_delete_order = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql_delete_order, (order_id,))

        # 문제 7: 특정 제품 검색
        sql_search_product = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql_search_product, ('%Book%'))
        for row in cursor.fetchall():
            print(row)

        # 문제 8: 특정 고객의 모든 주문 조회
        sql_select_orders_by_customer = "SELECT * FROM Orders WHERE customerID = %s"
        cursor.execute(sql_select_orders_by_customer, (customer_id,))
        for row in cursor.fetchall():
            print(row)

        # 문제 9: 가장 많이 주문한 고객 찾기
        sql_top_customer = """
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders 
        GROUP BY customerID 
        ORDER BY orderCount DESC 
        LIMIT 1
        """
        cursor.execute(sql_top_customer)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer[0]}, Orders: {top_customer[1]}")

    # 모든 변경사항 커밋
    conn.commit()

finally:
    conn.close()