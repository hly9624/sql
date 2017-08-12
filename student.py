#!/usr/bin/env python
#coding=utf-8

import MySQLdb
import getpass

password = getpass.getpass("please input your passworld:")

try:
    db = MySQLdb.connect('localhost','root',password,'stu')
except MySQLdb.ProgrammingError:
    exit(1)

cursor = db.cursor()



while (1 > 0):
    print "-----------------------command--------------------------"
    print "--1: insert  2: delete 3: update 4: select 5: quit------"
    print "--------------------------------------------------------"
    print "input command >>"


    num = input()

    if num == 1:
        print
        a = input("input id(int) >>")
        print "input name(string) >>"
        b = raw_input()
        print "input age(int) >>"
        c = input()
        print "input score(int) >>"
        d = input()
        sql = '''insert into tab values ("%d,%s,%d,%d")'''%(a,b,c,d)
        try:
            cursor.execute(sql)
            db.commit()
        except MySQLdb.ProgrammingError:
            db.rollback()
