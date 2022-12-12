import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200",
    database="runoob_db"
)
mycursor = mydb.cursor()

# 删除记录
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")
