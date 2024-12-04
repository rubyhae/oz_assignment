import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='oz-pasword',
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

#1
with connection.cursor() as cursor:
    sql = "insert into products (product_name, price, stock_quantity) values (%s, %s, %s)"
    cursor.excute(sql, ('Python Book', 29.99, 10))
    connection.commit()

    #2
    cursor.execute("select * from customers")
    for customers in cursor.fecthall():
        print(customers)

    #3
    sql = "update products set stock_quantity = stock_quantity - %s where productid = %s"
    cursor.execute(sql, (1, 1))
    connection.commit()

    #4
    sql = "select customerID, SUM(totalAmount) from Orders Group by customerID"
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(datas)

    #5
    sql = "update customers set email = %s where customerID = %s"
    cursor.execute(sql, ('johnnn@update.com'), 1)
    connection.commit()

    #6
    sql= "delete from orders where orderID = %s"
    cursor.execute(sql, (15))
    connection.commit()

    #7
    sql = "select * from products where product_name like %s"
    cursor.execute(sql, ('%Book%'))
    datas = cursor.fetchall()

    for data in datas:
        print(data ['product_name'])

    #8
    sql = "select * from orders where customerID = %s"
    cursor.execute(sql, (1))
    datas = cursor.fetchall()

    for data in datas:
        print(data)

    #9
    sql = """
        select customerID, count(*) as orderCount 
        from orders group by customerID 
        order by orderCount desc Limit 1
    """

    cursor.execute(sql)
    data = cursor.fetchone()

    print(data)


cursor.close()