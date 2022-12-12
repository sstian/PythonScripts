"""
2019.11.27 11.39
mysql-connector 连接使用 MySQL

安装：python -m pip install mysql-connector-python
"""

import mysql.connector


# 创建数据库连接
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200"
)

mycursor = mydb.cursor()

# 创建数据库
mycursor.execute("CREATE DATABASE runoob_db")


