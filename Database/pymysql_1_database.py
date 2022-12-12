"""
2019.11.27 12:21
Python3 MySQL 数据库连接 - PyMySQL 驱动

安装：pip3 install PyMySQL
"""

import pymysql


class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='5200', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    with DB(host='localhost',user='root',passwd='5200',db='runoob_db') as db:
        db.execute('SELECT * FROM sites')
        print(db)
        for i in db:
            print(i)
