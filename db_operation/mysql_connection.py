

import pymysql


# 打开数据库连接
db = pymysql.connect("localhost","llp","123456","world")

# 创建游标对象cursor
cursor = db.cursor()

# 使用excute方法执行查询
# cursor.execute("SELECT VERSION()")

# 单条查询
# data = cursor.fetchone()

# print("data:%s" %data)

sql = "SELECT * FROM CITY WHERE POPULATION > 10000000"

cursor.execute(sql)
results = cursor.fetchall()

for i in results:

    print(i)
# 关闭数据库
db.close()