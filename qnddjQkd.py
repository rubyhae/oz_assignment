import pymysql
from dummy import Dummy
from pymysql.cursors import DictCursor

# Faker 객체 생성
fake = Dummy

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
        
        # 더미 사용자 10명 데이터 삽입
        for i in range(10):
            print ("\n 회원 정보를 입력해주세요. \n")
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password = fake.password()
            gender = fake.choice()
            sql = 'INSERT INTO users (first_name, last_name, email, password, gender) VALUES (%s, %s, %s, %s, %s)'
            values = (first_name, last_name, email, password, gender)
            cursor.execute(sql,values)

        #재고 변동 이력 10개 생성
        for _ in range(10):
            raw_materials_id = fake.raw_materials_id() #원재료 아이디
            pre_quantity = fake.pre_quantity()
            quantity = fake.quantity()
            change_type = fake.change_type()
            store_id = fake.store_id()
            sql = 'INSERT INTO stocks (raw_materials_id, pre_quantity, quantity, change_type, store_id) VALUES (%s, %s, %s, %s, %s)'
            values = (raw_materials_id, pre_quantity, quantity, change_type, store_id)
            cursor.execute(sql,values)

        # sales_item 테이블에 데이터 추가하기
            sales_record_id = fake.sales_record_id()
            product_id = fake.product_id()
            quantity = fake.sales_quantity()
            sql = 'INSERT INTO sales_items (sales_record_id, product_id, quantity) VALUES (%s, %s, %s)'
            values = (sales_record_id, product_id, quantity)
            cursor.execute(sql,values)

        # 본인만의 시그니처 메뉴 추가하기
            name = fake.product_name()
            description = fake.description()
            price = fake.product_price()
            sql = 'INSERT INTO products (name, description, price) VALUES (%s, %s, %s)'
            values = (name, description, price)
            cursor.execute(sql,values)

        #user1과 user2를 각각 매장 id 5와 7에 소속되어있는 직원과 매니저로 변경하기
            #새로운 직원을 고용할 경우 새로 등록 및 변경
            sql = "UPDATE users SET is_staff = 'TRUE' where first_name in 'user1'"
            cursor.execute(sql)
            sql = "INSERT INTO employees (code, type, store_id) VALUES (123, 'STAFF', 5)"
            cursor.execute(sql)
            sql = "UPDATE users SET is_staff = 'TRUE' where first_name in 'user2'"
            cursor.execute(sql)
            sql = "INSERT INTO employees (code, type, store_id) VALUES (177, 'MANAGER', 7)"
            cursor.execute(sql)
            
            #기존에 employees로 등록된 사람에 대한 변경
            sql = "UPDATE employees SET store_id = 5, type = 'STAFF' , is_active = 'TRUE' WHERE user_id = (SELECT id FROM users WHERE first_name = 'user1' )"
            #set은 변경 영역, user1 이름을 가진 사람의 id를 찾아서 변경한다.
            cursor.execute(sql)
            sql = "UPDATE employees SET store_id = 7, type = 'MANAGER' , is_active = 'TRUE' WHERE user_id = (SELECT id FROM users WHERE first_name = 'user2' )"
            #set은 변경 영역, user1 이름을 가진 사람의 id를 찾아서 변경한다.
            cursor.execute(sql)

        print("all done")
        # # 변경 사항 커밋
        connection.commit()
finally:
    connection.close()
