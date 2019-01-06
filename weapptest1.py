#!/usr/bin/python
# -*- coding: UTF-8 -*-

# CGI处理模块
import cgi, cgitb

print "Content-type:text/html"
print
print "{\"data\':\"hello world weapp\"}"