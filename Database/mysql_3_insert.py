import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5200",
    database="runoob_db"
)
mycursor = mydb.cursor()

# 批量插入数据
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('RUNOOB', 'https://www.runoob.com'),
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/'),
    ('Zhihu', 'https://www.zhihu.com')
]

mycursor.executemany(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")
