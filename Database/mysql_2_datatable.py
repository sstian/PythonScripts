
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200",
    database="runoob_db")

mycursor = mydb.cursor()

# # 创建数据表
# mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
#
# # 添加主键
# mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# 创建数据表 主键
mycursor.execute("CREATE TABLE sites ("
                 "id INT AUTO_INCREMENT PRIMARY KEY, "
                 "name VARCHAR(255), "
                 "url VARCHAR(255))")
