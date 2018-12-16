#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb, MySQLdb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('logname')
site_pass  = form.getvalue('logpass')

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "PokerinDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
userPass = ""
# SQL 查询语句
sql = "SELECT userPass FROM UserInfo where userName='%s'" % (site_name)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   if results.hasNext():
       for row in results:
           userPass = row[0]

except:
   userPass = ""

if userPass == site_pass:
    result="success"
else:
    result="fail"

# 关闭数据库连接
cursor.close()
db.close()

print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset=\"utf-8\">"
print "<title>菜鸟教程 CGI 测试实例</title>"
print "</head>"
print "<body>"
print "<h2>%s</h2>" % (result)
print "</body>"
print "</html>"