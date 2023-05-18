# -*- coding = utf-8 -*-
# @author:   hanzhihchao7
# @date:     2023/2/23 20:23
# @File:     function_test.py
# @Software: PyCharm


# 必传参数
def add(a, b):
    return a + b


# 默认参数，调用该方法，不传参时使用默认参数
def add2(a=1, b=2):
    return a + b


def test_args(*args, **kwargs):
    print(args, type(args))  # (1, 2, 3, 4) <class 'tuple'>
    print(kwargs, type(kwargs))  # {'name': '测试', 'age': 15} <class 'dict'>


if __name__ == '__main__':
    print("必传参数测试：", add(4, 5))  # 9
    print("默认参数测试不传参：", add2())  # 3
    print("默认参数测试传参：", add2(4, 5))  # 9
    print("可变参数测试: ")
    test_args(1, 2, 3, 4, name='测试', age=15)
    # 正确传入元组和字典类型
    tuple_test = (1, 2, 3, 4)
    dict_test = {'name': '测试', 'age': 15}
    # 注： 用 * 和 ** 在对应传参的变量名进行标注
    test_args(*tuple_test, **dict_test)
