import pymysql
from pymysql.cursors import DictCursor

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host="localhost",
    user="root",  # 사용자 이름
    password="746472",  # 비밀번호
    database="db_test", # db 이름
    charset="utf8mb4",
    cursorclass=DictCursor
)

try:
    with connection.cursor() as cursor:

# 새로운 사용자 “8ki joa”를 추가해주세요.

        sql = " INSERT INTO USERS (first_name, last_name, email, password, address, contact, gender) VALUES (%s, %s, %s, %s, %s, %s, %s) "
        values = ('8ki', 'joa', 'joa8@test.com', 'joajoa88', 'address11', 'contact11', 'MALE')
        cursor.execute(sql, values)

# 사용자 “8ki joa”의 주소를 변경해주세요.
        sql = " UPDATE users SET address = 'address1122' WHERE first_name = (SELECT first_name FROM users WHERE firstname = '8ki' ) "
        cursor.execute(sql)

# 붕어빵 추가
    
    # 팥 붕어빵 추가 
        insert_product_1 = """ 
        INSERT INTO products (product_name, description, price) 
        VALUES ('팥 붕어빵', '팥이 가득 들어있는 팥붕', 1000); 
        """ 
        cursor.execute(insert_product_1) 
    
    # 크림 붕어빵 추가 
        insert_product_2 = """ 
        INSERT INTO products (product_name, description, price) 
        VALUES ('크림 붕어빵', '달콤한 크림이 가득 든 크붕', 1200);
        """ 
        cursor.execute(insert_product_2) 
    
    # 인절미 붕어빵 추가 
        insert_product_3 = """ 
        INSERT INTO products (product_name, description, price) 
        VALUES ('인절미 붕어빵', '쫀득한 떡이 들어있는 인절미 붕어빵', 1500); 
        """ 
        cursor.execute(insert_product_3)

# 사용자 “8ki joa”의 주문을 생성해주세요.
        sql = " INSERT INTO sales_record (user_id, store_id) VALUES (11, 5) "
        cursor.execute(sql)
        sql = " INSERT INTO sales_item (sales_record_id, product_id, quantity) VALUES (1, 1, 3)"
        cursor.execute(sql)
        sql = " INSERT INTO sales_item (sales_record_id, product_id, quantity) VALUES (2, 2, 2)"
        cursor.execute(sql)
        sql = " INSERT INTO sales_item (sales_record_id, product_id, quantity) VALUES (3, 3, 5)"
        cursor.execute(sql)

# raw_materials 추가
        sql = " INSERT INTO raw_materials (rm_name, price) VALUES ('팥', 1.57)"
        cursor.execute(sql)
        sql = " INSERT INTO raw_materials (rm_name, price) VALUES ('크림', 2.21)"
        cursor.execute(sql)
        sql = " INSERT INTO raw_materials (rm_name, price) VALUES ('인절미', 3.36)"
        cursor.execute(sql)

# order_records 테이블에 발주이력을 3건 생성해주세요.
        sql = " INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (1, 1, 1, 3)"
        cursor.execute(sql)
        sql = " INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (1, 3, 3, 2)"
        cursor.execute(sql)
        sql = " INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity) VALUES (1, 4, 4, 5)"
        cursor.execute(sql)

# daily_records 테이블에 원재료 사용이력을 3건 추가하고, 해당 추가 이력만큼 변동된 재고를 반영해 stocks 테이블에 새로운 데이터를 생성해주세요.
        sql = " INSERT INTO daily_record (rm_id, rm_name, quantity) VALUES (1, '팥', 3 )"
        cursor.execute(sql)
        sql = " INSERT INTO daily_record (rm_id, rm_name, quantity) VALUES (2, '크림', 2 )"
        cursor.execute(sql)
        sql = " INSERT INTO daily_record (rm_id, rm_name, quantity) VALUES (3, '인절미', 5 )"
        cursor.execute(sql)

# 팥 stocks
        sql = """ 
        UPDATE stock SET quantity = (SELECT quantity FROM stock where rm_id = 1) - 
        (SELECT quantity FROM daily_record where rm_id = 1), create_at = now()
        WHERE stock_id = (SELECT rm_id FROM daily_record where rm_id =1)
        """
        cursor.execute(sql)
# 크림 stocks
        sql = """ 
        UPDATE stock SET quantity = (SELECT quantity FROM stock where rm_id = 2) - 
        (SELECT quantity FROM daily_record where rm_id = 2), create_at = now()
        WHERE stock_id = (SELECT rm_id FROM daily_record where rm_id =2)
        """
        cursor.execute(sql)

# 인절미 stocks        
        sql = """ 
        UPDATE stock SET quantity = (SELECT quantity FROM stock where rm_id = 3) - 
        (SELECT quantity FROM daily_record where rm_id = 3), create_at = now()
        WHERE stock_id = (SELECT rm_id FROM daily_record where rm_id =3)
        """
        cursor.execute(sql)

        sql = " SELECT * FROM stock ORDER BY create_at DESC LIMIT 3 "
        cursor.execute(sql)
        
        show = cursor.fetchall()
        print(show)


    # 유저 “8ki joa”가 주문한 내역을 조회해주세요.
        sql = """
        SELECT product_name, sales_item.quantity, product.price
        FROM users
        JOIN sales_record on sales_record.user_id = user.id
        JOIN sales_items on sales_items.sales_record_id = sales_record.id
        JOIN products on products.id = sales_item.product_id
        WHERE user.first_name = '8ki'
        ORDER BY product.price DESC
        """
        cursor.execute(sql)

finally:
    connection.close()