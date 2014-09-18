#coding:utf-8

import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串” 
pattern = re.compile(r'hello')

match1 = pattern.match('hello world!') 
if match1:
	print match1.group()
else:
	print u'match1匹配失败'


match2 = pattern.match('helloo world!') 
if match2:
	print match2.group()
else:
	print u'match2匹配失败'


match3 = pattern.match('helllo world!') 
if match3:
	print match3.group()
else:
	print u'match3匹配失败'

