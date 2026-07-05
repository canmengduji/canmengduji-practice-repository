# bool突破

# BASCIAL KNOWLEDGE

'''
布尔型（bool）：布尔型只有True、False两种值，要么是True，要么是False，可以用来表示现实世界中的“是”和“否”，命题的“真”和“假”，状况的“好”与“坏”，水平的“高”与“低”等等。如果一个变量的值只有两种状态，我们就可以使用布尔型。
'''

"""
bool取值:bool 本身不会变，但很多其他类型的值（数字0、空字符串、空容器、None）在 if 或 bool() 中会被当做 False，非零、非空、非None则被当做 True。
"""

# 输出False的情况
print (bool(not True))  #主动取反
print (bool(0))       # False
print (bool(0.0))     # False
print (bool(None))    # False
print (bool(''))      # False（空字符串）
print (bool([]))      # False（空列表）
print (bool({}))      # False（空字典）
print (bool(set()))   # False（空集合）

# 输出True的情况
print (bool(1))       # True
print (bool(-1))      # True（非零都是True）
print (bool('hello')) # True（非空字符串）
print (bool([1,2]))   # True（非空列表）
print (bool({'a':1})) # True（非空字典)

# deepseek辅助↓

# bool与True,False的本质是数字(True,False不能写成true,false！)
print ("BOOL本质")
print (True+True)  # 为2
print (True*888)  # 为1*888=888
print (False-1000)  # 为0-1000=-1000
print (555*False)  # 为555*0=0

# 条件判断中，非空为真
print ("条件判断中，非空为真")
if "hello":
    print("非空字符串 → True")
if []:
    print("空列表 → False，这行不会执行")
if 5:
    print("非零数字 → True")

# 比较运算（> < == !=）返回 bool

print("比较运算返回 bool")
print(5 > 3)     # True
print(5 == 3)    # False
print(type(5 > 3))  # <class 'bool'>

age = int (input ("你的年龄"))
if age < 18 :
    print ("未成年")
else :     # else为“否则”，否定最近上一个条件
    print ("已成年")





'''
Run Successfully
➜ ~ python /storage/emulated/0/python/Essay5.py
False
False
False
False
False
False
False
False
True
True
True
True
True
BOOL本质
2
888
-1000
0
条件判断中，非空为真
非空字符串 → True
非零数字 → True
比较运算返回 bool
True
False
<class 'bool'>
你的年龄15
未成年
➜ ~
'''