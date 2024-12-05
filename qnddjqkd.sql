import random

import pymysql
from faker import Faker
from pymysql.cursors import DictCursor

fake = faker

connection = pymysql.connect(
    host="localhost",
    user="root",  # 사용자 이름
    password="0000",  # 비밀번호
    database="db_name", # db 이름
    charset="utf8mb4",
    cursorclass=DictCursor,
)

try:
    with connection.cursor() as cursor:
        for _ in range(10):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.unique.email()
            password = fake.password()
            address = fake.address()
            contact = fake.phone_number()
            gender = random.choice(["MALE", "FEMALE"])

            cursor.execute(
                """
                INSERT INTO users (first_name, last_name, email, password, address, contact, gender)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
                (first_name, last_name, email, password, address, contact, gender),
            )

        for _ in range(5):
            name = fake.country()
            address = fake.address()
            contact = fake.phone_number()

            cursor.execute(
                """
                INSERT INTO stores (name, address, contact)
                VALUES (%s, %s, %s)
            """,
                (name, address, contact),
            )