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
    for row in range(0,len(matrix_list)):
        for column in range(row, len(matrix_list)):
            matrix_list[row][column], matrix_list[column][row] = matrix_list[column][row], matrix_list[row][column]
    return matrix_list
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
#以矩阵的形式打出来
for item in matrix_transposition(list01):
    for i in item:
        print(i, end=" ")
    print(" ")