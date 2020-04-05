"""
数据库操作
"""

import pymysql
from __init__ import MYSQL_USER,MYSQL_PASSWD


class UserDao:

    def __init__(self):
        self.connect = pymysql.connect("localhost",user=MYSQL_USER,passwd=MYSQL_PASSWD,db="happywater")

    def query_one_by_account(self,_account):
        """

        :param _account:
        :return: 返回元组 （value, value） 根据select
        """
        cursor = self.connect.cursor()
        sql = "select uaddress,uname,uforce from user where uaddress='{}'".format(_account)
        affeted = cursor.execute(sql)
        if affeted > 0:
            res = cursor.fetchone()
        cursor.close()
        return res


    def insert_one(self, user):
        cursor = self.connect.cursor()
        sql = "insert into user(uaddress,uname,uforce,uip) values('{}','{}',{},'{}')" \
                .format(user.account,user.name,user.force,user.ip)
        res = cursor.execute(sql)
        self.connect.commit()
        cursor.close()
        return res

    def update_force(self, _account, _force):
        """
        更新force
        :param _account:
        :param _force:
        :return:
        """
        cursor = self.connect.cursor()
        sql = "update user set uforce={} where uaddress='{}'".format(_force, _account)
        affected = cursor.execute(sql)
        self.connect.commit()
        cursor.close()
        return affected

    def query_all(self):
        cursor = self.connect.cursor()
        sql = "select uname,uforce from user ORDER BY uforce DESC"
        affeted = cursor.execute(sql)
        if affeted > 0:
            res = cursor.fetchall()
        cursor.close()
        return res

    def close(self):
        self.connect.close()

