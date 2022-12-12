import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200",
    database="runoob_db"
)

mycursor = mydb.cursor()

# 删除表
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
mycursor.execute(sql)
