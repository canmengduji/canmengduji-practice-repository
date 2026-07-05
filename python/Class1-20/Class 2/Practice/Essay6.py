"""
规则部分：

规则1：变量名由字母、数字和下划线构成，数字不能开头。需要说明的是，这里说的字母指的是 Unicode 字符，Unicode 称为万国码，囊括了世界上大部分的文字系统，这也就意味着中文、日文、希腊字母等都可以作为变量名中的字符，但是一些特殊字符（如：！、@、#等）是不能出现在变量名中的。我们强烈建议大家把这里说的字母理解为尽可能只使用英文字母。

规则2：Python 是大小写敏感的编程语言，简单的说就是大写的A和小写的a是两个不同的变量，这一条其实并不算规则，而是需要大家注意的地方。

规则3：变量名不要跟 Python 的关键字重名，尽可能避开 Python 的保留字。这里的关键字是指在 Python 程序中有特殊含义的单词（如：is、if、else、for、while、True、False等），保留字主要指 Python 语言内置函数、内置模块等的名字（如：int、print、input、str、math、os等）。

惯例部分：

惯例1：变量名通常使用小写英文字母，多个单词用下划线进行连接。

惯例2：受保护的变量用单个下划线开头。

惯例3：私有的变量用两个下划线开头。

惯例2和惯例3大家暂时不用管，讲到后面自然会明白的。当然，作为一个专业的程序员，给变量命名时做到见名知意也是非常重要，这彰显了一个程序员的专业气质，很多开发岗位的面试也非常看重这一点。
"""

# Part 1
print ("大小写敏感")
ai_deepseek = 100
AI_DeepSeek = 200
SB_DeepSeek = 300
print (ai_deepseek)
print (AI_DeepSeek)
print (SB_DeepSeek)

# Part 2
print ("见名知意")
name = "DeepSeek V4"
age = 3
参数 = "1.6T-284B"

print (f"名字 : {name},年龄 : {age},参数 : {参数}")



"""
Run Successfully
➜ ~ python /storage/emulated/0/python/Essay6.py
大小写敏感
100
200
300
见名知意
名字 : DeepSeek V4,年龄 : 3,参数 : 1.6T-284B
➜ ~
"""