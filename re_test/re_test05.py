#coding:utf-8

import re

import re  
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)  
   
print "p.pattern:", p.pattern  
print "p.flags:", p.flags  
print "p.groups:", p.groups  
print "p.groupindex:", p.groupindex  

