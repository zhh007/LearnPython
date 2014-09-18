#coding:utf-8

import re

p = re.compile(r'\d+')  
print p.findall('one1two2three3four4')  

p = re.compile(r'\d+')  
for m in p.finditer('one1two2three3four4'):  
    print m.group(), 

