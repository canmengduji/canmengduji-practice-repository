# Day3综合实践˶>ᗜ<˶

# Essay1-6's Improvementᜊ•͈⌔•͈ᜊ

# 场景 : 图书馆借阅书籍

"""
Program 1 : 借阅登记₍ᵔ･•･ᵔ₎
书名的变量命名使用bookname
借阅书本数量使用number作为变量，这里需要转化为数字
这个天数用int函数转为数字，使用day为变量
逾期费用说明使用print()+float()输出提示
(借阅书本数量是后面想出来的,那么我们在这里还需要运用到数学运算,决定借阅的逾期费用计算为一本书为10元,根据数量为10元乘以Number)，变量命名为money

Program 2 : 是否逾期与逾期费用计算ᔦ ° ꒳ ° ᔨ ̖́-
实际借用天数为fact_day
使用判断函数<>=，通过我初步学习的if,else进行判断

Design Firstly :
bookname = str (input ("你的书名"))
number = int (input ("书本数量"))
day = int (input ("借阅天数"))
"""

# Part 1
print ("图书馆书本借阅")

bookname = input ("你的书名:")  # 由于input反回字符串，则去除str
number = int (input ("书本数量:"))  # 只能整型，总不能借0.5本<(ºOº)>
day = float (input ("借阅天数:"))

money = 10*number  # 原本是money=({day}*{number}),但看到下面这个的格式,所以我赌一把

print (f"书名 : {bookname},书本数量 : {number},借阅天数 : {day},逾期费用(按天记) : {money}")

# Part 2

fact_day = float (input ("实际借阅天数:"))

if fact_day <= day :
    print ("You are honest¯꒳¯")
else :
    out_day = fact_day - day
    fine = money*out_day
    print (fine)




"""
你原先犯的错误f"?"是字符串,想复杂了吗？
money = (f"10*{number}")   # ❌ 这是字符串，不是数字money = (f"10*{number}")   # ❌ 这是字符串，不是数字

if fact_day <= number :   # ✅ 这行判断是对的
    print ("You are honest")
else :
    out_day = (f"{fact_day}-{day}")   # ❌ 字符串
    fine = (f"{money}*{out_day}")     # ❌ 字符串
    print (fine)
"""


# Debug 测试阶段一


"""
第一次运行: 尝试的超纲内容,学到了
➜ ~ python /storage/emulated/0/python/Essay7.py
  File "/storage/emulated/0/python/Essay7.py", line 39
    if fact_day =< number :
                ^
SyntaxError: invalid syntax

第二次运行:有些输出有问题，说明是代码的问题
➜ ~ python /storage/emulated/0/python/Essay7.py
你的书名:深度思考
书本数量:1
借阅天数:5
书名 : 深度思考,书本数量 : 1,借阅天数 : 5.0,逾期费用(按天记) : 10*1
实际借阅天数:8
10*1*8.0-5.0
第三次运行:没有逾期，输出正常
➜ ~ python /storage/emulated/0/python/Essay7.py
你的书名:DeepSeek
书本数量:1
借阅天数:5
书名 : DeepSeek,书本数量 : 1,借阅天数 : 5.0,逾期费用(按天记) : 10*1
实际借阅天数:1
You are honest¯꒳¯
➜ ~
"""


# Debug 测试阶段二


"""
第二次测试:

第一次运行: 实际天数与计划天数的比较写成了实际天数比较书本数量→向Ds求助
➜ ~ python /storage/emulated/0/python/Essay7.py
你的书名:深度求索,Transformer,物理渲染
书本数量:3
借阅天数:45
书名 : 深度求索,Tran物理渲,书本数量 : 3,借阅天数 : 45.0,逾期费用(按天记) : 30
实际借阅天数:44
-30.0

第二次运行:Run Successfully
➜ ~ python /storage/emulated/0/python/Essay7.py
你的书名:深度求索,Transformer,物理渲染
书本数量:3
借阅天数:45
书名 : 深度求索,Transformer,物理渲染,书本数量 : 3,借阅天数 : 45.0,逾期费用(按天记) : 30
实际借阅天数:44
You are honest¯꒳¯

第三次运行:Run Successfully 这额度有点大呀<(ºOº)>，我们要做诚实的好孩子
➜ ~ python /storage/emulated/0/python/Essay7.py
你的书名:深度求索,Transformer,物理渲染
书本数量:3
借阅天数:45
书名 : 深度求索,Transformer,物理渲染,书本数量 : 3,借阅天数 : 45.0,逾期费用(按天记) : 30
实际借阅天数:90
1350.0
➜ ~
"""