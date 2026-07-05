"""
字符串型（str）：
字符串是以单引号或双引号包裹起来的任意文本
比如'hello'和"hello"
"""

'hello,python'

"hello,friend"

"""
布尔型（bool）：
布尔型只有True、False两种值，要么是True，要么是False，可以用来表示现实世界中的“是”和“否”，命题的“真”和“假”，状况的“好”与“坏”，水平的“高”与“低”等等。
如果一个变量的值只有两种状态(应用条件)，我们就可以使用布尔型。
"""

"""
bool取值
"""

# 输出False的情况

bool (not True)  #主动取反
bool(0)       # False
bool(0.0)     # False
bool(None)    # False
bool('')      # False（空字符串）
bool([])      # False（空列表）
bool({})      # False（空字典）
bool(set())   # False（空集合）

# 输出True的情况

bool(1)       # True
bool(-1)      # True（非零都是True）
bool('hello') # True（非空字符串）
bool([1,2])   # True（非空列表）
bool({'a':1}) # True（非空字典）

"""
总结:
bool 本身不会变，但很多其他类型的值（数字0、空字符串、空容器、None）在 if 或 bool() 中会被当做 False，非零、非空、非None则被当做 True。
"""