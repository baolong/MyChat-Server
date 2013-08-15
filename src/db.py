#!/usr/bin/env python
#_*_ coding:utf-8

import MySQLdb

class DB(object):
    def __init__(self):
        self.cxn = MySQLdb.connect(db='mychat')
#        self.cur = self.cxn.cursor()
#        self.cur.execute('CREATE TABLE userlist(user VARCHAR(15), passwd VARCHAR(15))')
#        self.cur.execute('CREATE TABLE friendlist(uername VARCHAR(15), friendsname VARCHARa(15))')
#        self.cur.close()
#        self.cxn.commit()

    def db_addNewUser(self, username, passwd):
        self.cur = self.cxn.cursor()
        self.cur.execute('INSERT INTO userlist VALUES(' + username + ',' \
                    + passwd + ')')
        self.cur.close()
        self.cxn.commit()

    

