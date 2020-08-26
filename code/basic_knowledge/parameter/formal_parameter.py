"""
函数传递
   形式参数
"""

def fun01(a=None,b=0,c=2,d=7):
    print(a)
    print(b)
    print(c)
    print(d)

#1. 缺省（默认）参数：如果实参不提供，可以使用默认值
#关键字实参+缺省形参=调用者可以随意传递参数
fun01(c=2,b=3)

#练习：定义函数，根据小时 分钟 秒 计算总秒数，要求可以灵活计算秒数
def time_calculator(hour = 0, minute = 0, second=0):
    return hour * 3600 + minute * 60 + second
print(time_calculator(hour=1,second=10))

# 2. 位置形参
def fun02(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

# 3.星号元组形参: * 将所有实参合并为一个元组
# 作用：让实参个数无限
def fun03(*args):#arg--argument形参的意思，一般这个地方要写成args这样
    print(args)

#练习：定义数值相加的函数
def sum_num(*args):
    sum = 0
    for item in args:
        sum += item
    print(sum)
sum_num(2,3,567,34)

# 4.命名关键字形参:在星号元组形参以后的位置形参
# 目的：要求实参必须使用关键字实参.
def fun04(a, *args, b):#这种方式a,b至少是要有值的
    print(a)
    print(args)
    print(b)
fun04(1, b=2)
fun04(1, 2, 3, 4, b=2)

#或
def fun05(*, a, b):
    print(a)
    print(b)
fun05(a=1, b=2)

# 5. 双星号字典形参：**目的是将实参合并为字典.
#               实参可以传递数量无限的关键字实参.