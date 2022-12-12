import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200",
    database="runoob_db"
)
mycursor = mydb.cursor()

# 查询记录
sql = "SELECT * FROM sites"
# sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
mycursor.execute(sql)

myresult = mycursor.fetchall()  # fetchall() 获取所有记录
# myresult = mycursor.fetchone()  # fetchone() 读取一条记录

for x in myresult:
    print(x)
