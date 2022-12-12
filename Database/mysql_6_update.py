import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200",
    database="runoob_db"
)

mycursor = mydb.cursor()

# 更新记录
# 防止数据库查询发生 SQL 注入的攻击，可以使用 %s 占位符来转义更新语句的条件
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")
