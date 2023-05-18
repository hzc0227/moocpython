# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/2 10:16
# @File:     grammar.py
# @Software: PyCharm

# def = '1'
#
# if __name__ == '__main__':
#     print(def)

# print = '1'
#
# if __name__ == '__main__':
#     print(1)

# test_list = [1, 2, 3, '4', "哈喽"]

# if __name__ == '__main__':
#     print('max -', max(test_list))
#     print('min -', min(test_list))

# test_tuple = ([1, 2, 3], [4, 5, 6])
#
#
# if __name__ == '__main__':
#     print(test_tuple[1])  # [4, 5, 6]
#     test_tuple[1][1] = 8
#     print(test_tuple[1])  # [4, 8, 6]
#     print("123" * 10)

# ss = '\nA:\n\n①PT菜单-PT设置-多语言。②选择启用多语言用户界面③新建,输入语言名称和值,不同语言设置不同值，例如中文值0，英文值1。\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0④PT菜单-PT设置-标准，设置控制区域地址和大小为8，例如DM0。⑤在功能对象的属性-标签，分别输入中文和英文。\xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0 \xa0⑥通过按钮或者数据输入，修改控制区域地址+7，即DM7数据，DM7=0显示中文，DM7=1显示英文。\n\n\n'
# sss = ss.replace('\\xa0', '').replace('\\n', '').replace(' ','').replace('A:', '')
# print(sss)
string = 'ceshi'
print(string.capitalize())

string = 'aBc'
new_string = string.swapcase()
new_string2 = string.zfill(10)
print(string)  # aBc
print(new_string)  # AbC
print(new_string2)
print(new_string2.count('0'))

strs = 'aacbbaac'
print(strs.strip('aac'))

data = []
# data.append({"2": 2})
if not data:
    data.append({"1": ''})
data[0].update({"1": 2})
print(data)
