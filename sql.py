#!/usr/bin/env python
#coding=utf-8

import MySQLdb
import getpass

password = getpass.getpass("please input your password:")

#打开数据库链接
try:
    db = MySQLdb.connect('localhost','root',password,'stu')
except ProgrammingError:
    exit(1)

#获取数据库游标
cursor = db.cursor()    #名字随便起


#执行数据库sql语句
cursor.execute("select version()")

#得到语句执行结果

data = cursor.fetchone()

print "database :",data



cursor.execute("drop table if exists newtab")

sql = '''create table newtab (first_name char(20) not null,
        last_name char(20),
        age int,
        sex char(2)
        )'''

cursor.execute(sql)


sql = '''insert into newtab values ('Mac','Mohan',20,'M')'''

try:
    cursor.execute(sql)
    db.commit()
except MySQLdb.ProgrammingError:
    db.rollback()

sql = "update newtad set age = age + 1 where sex = 'm'"
try:
    cursor.execute(sql)
    db.commit()
except MySQLdb.ProgrammingError:
    db.rollback()

sql = "delete from newtab where age > 20"
try:
    cursor.execute(sql)
    db.commit()
except MySQLdb.ProgrammingError:
    db.rollback()
db.close()
