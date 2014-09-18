
import urllib
import urllib2

url = "http://www.somehost.com/test.cgi"

values = {'name': 'abc', 'age': 2, 'language': 'python'}

data = urllib.urlencode(values)
req = urllib2.Request(url, data) #Post方式发送数据
response = urllib2.urlopen(req)
html = response.read()

print html


