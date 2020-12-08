# -*- coding: utf-8 -*-
import pymysql


# 构造函数初始化参数
class MysqlHelper:
    def __init__(self, host, port, db, user, passwd, charset):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def open(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def ex(self, sql):
        try:
            self.open()
            self.cursor.execute(sql)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)

    def all(self, sql):
        try:
            self.open()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)
