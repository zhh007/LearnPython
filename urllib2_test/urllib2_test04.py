
import urllib
import urllib2

data = {}

data['name'] = 'abc'
data['age'] = 21
data['language'] = 'python'

url_values = urllib.urlencode(data)
print url_values

url = "http://www.somehost.com/test.cgi"
full_url = url + '?' + url_values

req = urllib2.Request(full_url)
response = urllib2.urlopen(req) #Get方式发送数据
html = response.read()
print html
