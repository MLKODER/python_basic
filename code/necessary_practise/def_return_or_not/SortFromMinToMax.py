"""
用函数的形式对传入的列表进行升序排列
可以通过画内存图的方式，分析方法二
"""
#方法一
def minToMaxOrder(listA):
    for line in range(0, len(listA)-1):
        for column in range(line+1, len(listA)):
            if listA[line] > listA[column]:
                listA[line], listA[column] = listA[column], listA[line]
    return listA
list01 = [10, 34, 7, 199, 66]
print(minToMaxOrder(list01))


#方法二
def minToMaxOrder(listA):
    #满足以下两个条件就无需通过返回值return传递
    #1.传入的是可变对象
    #2.函数体修改的是传入的对象
    for line in range(0, len(listA)-1):
        for column in range(line+1, len(listA)):
            if listA[line] > listA[column]:
                listA[line], listA[column] = listA[column], listA[line]
list01 = [10, 34, 7, 199, 66]
#与上面的方式相比，这里直接通过函数方法体以后，要直接打印输出该函数，而不是print(minToMaxOrder(list01))，这样会返回none值
minToMaxOrder(list01)
print(list01)