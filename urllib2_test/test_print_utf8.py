#coding:utf-8

#import sys
#print sys.getdefaultencoding()
#reload(sys)
#sys.setdefaultencoding('utf-8') #允许打印unicode字符

print '======================'

str1 = '中文1'
print str1						#cmd下输出乱码
print type(str1)
u1 = str1.decode('utf-8')		#采用utf-8字符集解码
print type(u1)					#输出unicode
print u1


print '======================'
u3 = u'中文2'        			#创建unicode对象
print type(u3)
print u3


print '======================'
str1 = 'Hello World.'
ustr2 = u'服务器无法处理请求'

if isinstance(ustr2, unicode): 
	#s=u"中文" 
	print ustr2.encode('gb2312') 
else: 
	#s="中文" 
	print ustr2.decode('utf-8').encode('gb2312')


