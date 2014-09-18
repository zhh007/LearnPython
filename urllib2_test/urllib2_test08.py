#coding:utf-8

from urllib2 import Request, urlopen, URLError, HTTPError

req = Request('http://bbs.csdn.net/callabc')

try:
	response = urlopen(req)
except HTTPError, e:
	print 'The server couldn\'t fulfill the request.'
	print 'Error Code:', e.code
	

except URLError, e:
	print 'We failed to reach a server.'
	print 'Reason:', e.reason
	

else:
	print 'No exception was raised.'

