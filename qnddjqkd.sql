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

