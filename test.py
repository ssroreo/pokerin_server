#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("106.12.95.107", "PokerinDB", "root", "123456", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT userPass FROM UserInfo"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      # 打印结果
      print "fname=%s,lname=%s,age=%s" % \
             (fname, lname, age, )
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
cursor.close()
db.close()