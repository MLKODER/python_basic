"""
矩阵的转置
写一个函数，能够对任何正方矩阵进行转置
例如4阶矩阵：
[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]
"""
#以下这段函数可以通过一个一个推导写出来
def matrix_transposition(matrix_list):
    #也可以从0开始取，但是这样不好，因为多执行了n次对调，所以row从1开始取
    for row in range(1,len(matrix_list)):
        for column in range(row, len(matrix_list)):
            matrix_list[row-1][column], matrix_list[column][row-1] = matrix_list[column][row-1], matrix_list[row-1][column]
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
#以矩阵的形式打出来
matrix_transposition(list01)
for item in list01:
    for i in item:
        print(i, end=" ")
    print(" ")