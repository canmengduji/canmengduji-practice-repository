# str突破

a = input ("输入区:")
print (a)
# 说明:input()只反回字符串型(str)
# 所以Essay1~3使用了其他变量转化函数
# 所以在这里我直接print (a)而不是使用str()→print (str (a))使用

b = int (input ("Please type into number:"))
c = float (input ("Please type into any number:"))

print (str (b))
print (str (c))

# 字符串也可用“ ' ”或“ " ”表示
# deepseek金牌辅助˶>ᗜ<˶补充的内容

print("========== 1. 拼接 ==========")
print("你好" + "世界")

print("\n========== 2. 重复 ==========")
print("哈哈" * 3)

# This knowledge can give up.
# I can learn it across other classes.

"""
print("\n========== 3. 转义 ==========")
print("第一行\n第二行")
print("姓名\t年龄\t成绩")

print("\n========== 4. 长度 ==========")
print(len("Python"))

print("\n========== 5. 索引 ==========")
s = "Python"
print(s[0])
print(s[5])
"""




'''
Run Successfully
➜ ~ python /storage/emulated/0/python/Essay4.py
输入区:潜行者113
潜行者113
Please type into number:55
Please type into any number:888
55
888.0
========== 1. 拼接 ==========
你好世界

========== 2. 重复 ==========
哈哈哈哈哈哈
➜ ~
'''