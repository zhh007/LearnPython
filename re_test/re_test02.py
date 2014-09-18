#coding:utf-8

import re

"""
re.compile(strPattern[, flag]):
这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。
第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。
另外，你也可以在regex字符串中指定模式，
比如re.compile('pattern', re.I | re.M)与re.compile('(?im)pattern')是等价的。
可选值有：
    re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
    re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
    re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
    re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
    re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
    re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
以下两个正则表达式是等价的。
"""

a = re.compile(r"""\d +  # the integral part 
                   \.    # the decimal point 
                   \d *  # some fractional digits""", re.X)  
  
b = re.compile(r"\d+\.\d*")  
  
match11 = a.match('3.1415')  
match12 = a.match('33')  
match21 = b.match('3.1415')  
match22 = b.match('33')   
  
if match11:  
    # 使用Match获得分组信息  
    print match11.group()  
else:  
    print u'match11不是小数'  
      
if match12:  
    # 使用Match获得分组信息  
    print match12.group()  
else:  
    print u'match12不是小数'  
      
if match21:  
    # 使用Match获得分组信息  
    print match21.group()  
else:  
    print u'match21不是小数'  
  
if match22:  
    # 使用Match获得分组信息  
    print match22.group()  
else:  
    print u'match22不是小数'  