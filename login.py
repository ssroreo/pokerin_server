#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb, MySQLdb

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('logname')
site_pass  = form.getvalue('logpass')

db = MySQLdb.connect("localhost","root","123456","PokerinDB",charset="utf-8")

cursor = db.cursor()

sql="select userPass from UserInfo where userName='%s'" % (site_name)

cursor.execute(sql)

userPass = cursor.fetchone()

if userPass == site_pass:
    result="success"
else:
    result="fail"
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
print "<h2>%s%s</h2>" % (result)
print "</body>"
print "</html>"