#coding:utf-8

import urllib2

req = urllib2.Request('http://bbs.csdn.net/callabc')

try:
	urllib2.urlopen(req)
except urllib2.URLError, e:
	print e.code
	#print e.read()