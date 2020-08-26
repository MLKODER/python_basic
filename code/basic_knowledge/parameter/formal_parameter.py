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
    second_total = hour * 3600 + minute * 60 + second
    return second_total
print(time_calculator(hour=1,second=10))
