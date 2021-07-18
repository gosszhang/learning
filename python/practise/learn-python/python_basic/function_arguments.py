#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    function_arguments.py
 @Function:    python function arguments
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/4
"""

"""一、函数的调用之位置实参"""

"""
    调用函数时，可以根据每个形参在所有形参中的位置传递对应位置的实参，从而用每个实参初始化
    对应位置的形参，这样的实参称为位置实参
"""

def f(a, b, c):
    print('a =', a, 'b =', b, 'c = ', c)

f(2, 5, 8)  # a = 2 b = 5 c =  8

f(5, 8, 2)  # a = 5 b = 8 c =  2

f(8, 5, 2)  # a = 8 b = 5 c =  2


"""二、函数的调用之关键字实参"""

"""
    调用函数时，传递的实参的形式可以为：形参名 = 实参值，从而用指定的实参值初始化指定名称的形参，
    这样的实参称为关键字实参
"""

def f(a, b, c):
    print('a = ', a, 'b = ', b, 'c = ', c)

f(a = 2, b = 5, c = 8)  # a =  2 b =  5 c =  8

"""
    由于关键字实参中指定了形参名，所有实参和形参的匹配关系更加清晰，而且每个关键字实参在所有
    关键字实参中的位置可以是任意的
"""

f(b = 5, c = 8, a = 2)  # a =  2 b =  5 c =  8

f(c = 8, b = 5, a = 2)  # a =  2 b =  5 c =  8

"""
    调用函数时，可以组合使用位置实参和关键字实参。但是，位置实参必须位于关键字实参之前，否则，
    无法根据位置来匹配实参和对应的形参
"""

f(2, 5, c = 8)  # a =  2 b =  5 c =  8
# f(2, c = 8, 5)  # SyntaxError: positional argument follows keyword argument


"""三、函数的调用之实参的传递"""

"""
    前面学习过："变量相当于标签。对于赋值语句：变量 = 对象，相当于给对象贴了一个标签，
    标签名就是变量名"
    调用函数时把实参传递给形参从而用实参初始化形参，本质上执行了赋值语句：形参 = 实参对象，
    相当于给实参对象贴了一个标签，标签名就是形参名
    如果实参对象是可变类型，在函数体内对形参对象的任何修改其实就是对实参对象的修改
"""

def f(arg1, arg2):
    print('初始化形参后：arg1 =', arg1, 'arg2 =', arg2)
    arg1 = arg1 * 2
    arg2.append(4)
    print('修改形参后：arg1 =', arg1, 'arg2 =', arg2)

i = 10
L = [1, 2, 3]
print('调用函数前: i =', i, 'L =', L)    # 调用函数前: i = 10 L = [1, 2, 3]

f(i, L)
# 初始化形参后：arg1 = 10 arg2 = [1, 2, 3]
# 修改形参后：arg1 = 20 arg2 = [1, 2, 3, 4]

print('调用函数后：i =', i, 'L =', L)    # 调用函数后：i = 10 L = [1, 2, 3, 4]

i = 10
L = [1, 2, 3]
print('调用函数前: i =', i, 'L =', L)    # 调用函数前: i = 10 L = [1, 2, 3]

f(i, L[:])
# 初始化形参后：arg1 = 10 arg2 = [1, 2, 3]
# 修改形参后：arg1 = 20 arg2 = [1, 2, 3, 4]

print('调用函数后：i =', i, 'L =', L)    # 调用函数后：i = 10 L = [1, 2, 3]