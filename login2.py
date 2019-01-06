#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb, MySQLdb

print "Content-type:text/html"
print
print "{\"event\":\"login\"}"