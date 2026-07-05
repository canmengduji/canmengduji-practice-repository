# float突破

a = float (input ("输入数字:"))

b = float (input ("输入数字e数字:"))

print (a)
print (b)

"""
Mistake Summery:
print(be2)
 NameError: name 'be2' is not defined
 变量名写错，b 误写成 be2

float(input(...),e2)
SyntaxError / NameError
float() 只需要1个参数，多写了,e2

float()与eNUMBER结合转化要么固定写死，要么让用户输入number+e+number的科学计数法形式
"""


"""
成功的2次运行
➜ ~ python /storage/emulated/0/python/Essay3.py
输入数字:55
输入数字e数字:55e2
55.0
5500.0
➜ ~ python /storage/emulated/0/python/Essay3.py
输入数字:888888
输入数字e数字:8888e2
888888.0
888800.0
➜ ~
"""