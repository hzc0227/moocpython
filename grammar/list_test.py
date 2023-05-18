# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/7 9:46
# @File:     list_test.py
# @Software: PyCharm


# 测试二次赋值
import copy
import re

list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(list_a)  # [1, 2, 3, 4]
print(list_b)  # [1, 2, 3, 4]

# 测试copy函数
list_copy_a = [1, 2, 3]
list_copy_b = list_copy_a.copy()
print(list_copy_a)  # [1, 2, 3]
print(list_copy_b)  # [1, 2, 3]

