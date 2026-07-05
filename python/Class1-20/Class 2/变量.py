"""
①变量名由字母、数字和下划线构成，数字不能开头。需要说明的是，这里说的字母指的是 Unicode 字符
(Unicode 称为万国码，囊括了世界上大部分的文字系统，这也就意味着中文、日文、希腊字母等都可以作为变量名中的字符，但是一些特殊字符（如：！、@、#等）是不能出现在变量名中的)
我们强烈建议大家把这里说的字母理解为尽可能只使用英文字母。
②规则2：Python 是大小写敏感的编程语言，简单的说就是大写的A和小写的a是两个不同的变量，这一条其实并不算规则，而是需要大家注意的地方。
③规则3：变量名不要跟 Python 的关键字重名，尽可能避开 Python 的保留字。这里的关键字是指在 Python 程序中有特殊含义的单词（如：is、if、else、for、while、True、False等），保留字主要指 Python 语言内置函数、内置模块等的名字（如：int、print、input、str、math、os等）。
惯例部分：
①惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。
②惯例2：受保护的变量用单个下划线开头。
③惯例3：私有的变量用两个下划线开头。
"""

# 使用变量保存数据并进行加减乘除运算
# Version: 1.0
# Author: 骆昊
a = 45     # 定义变量a，赋值45
b = 12     # 定义变量b，赋值12
print(a, b)   # 45 12
print(a + b)  # 57
print(a - b)  # 33
print(a * b)  # 540
print(a / b)  # 3.75


# type函数检查变量类型
# Version: 1.0
# Author: 骆昊

a = 100
b = 123.45
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

# 变量类型的转换

"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串（在可能的情况下）转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码方式。
chr()：将整数（字符编码）转换成对应的（一个字符的）字符串。
ord()：将（一个字符的）字符串转换成对应的整数（字符编码）。
"""

# Version: 1.0
# Author: 骆昊

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int类型的100转成float，输出100.0
print(int(b))           # float类型的123.45转成int，输出123
print(int(c))           # str类型的'123'转成int，输出123
print(int(c, base=16))  # str类型的'123'按十六进制转成int，输出291
print(int(d, base=2))   # str类型的'100'按二进制转成int，输出4
print(float(e))         # str类型的'123.45'转成float，输出123.45
print(bool(f))          # str类型的'hello, world'转成bool，输出True
print(int(g))           # bool类型的True转成int，输出1
print(chr(a))           # int类型的100转成str，输出'd'
print(ord('d'))         # str类型的'd'转成int，输出100