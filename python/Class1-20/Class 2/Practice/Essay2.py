# INT之进制转换
print ("--------进制转换--------")

a = input ("输入由0,1组成的数字˶>ᗜ<˶:")

b = input ("输入由0-7组成的数字˶>ᗜ<˶:")

c = input ("Please type into any number˶>ᗜ<˶:")

d = input ("Please type into number between 0-9 and A-F˶>ᗜ<˶:")

# 2进制转10进制

print (int (a,2))

# 0b后只能加由0,1组成的NUMBER,所以无法使用
# 而int转进制有别的形式int (变量名,2)
# 0b转化的标准形式，以1010为例
# print (0b1010)→输出10

# 8进制转10进制

print (int (b,8))

# 同理0o后只能加0-7的NUMBER
# print (0o100)→输出64

# 10进制

print (int (c,10))

# 16进制转10进制

print (int (d,16))

# 0x后加0-9和A-F，不可有空格
# print(0x100)   输出 256（十六进制100 = 十进制256）
# print(0xFF)    输出 255（十六进制FF = 十进制255）
# print(0x10)    输出 16（十六进制10 = 十进制16）