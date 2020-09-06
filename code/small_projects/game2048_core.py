"""
2048  游戏核心算法
"""
# 练习１：零元素移至末尾
# 　　[2,0,2,0]  --> [2,2,0,0]
#    [2,0,0,2]  --> [2,2,0,0]
#    [2,4,0,2]  --> [2,4,2,0]

#思想一：从前往后，两个for循环遍历，逐个移动
def move_zero_bottom(listA):
    for c in range(len(listA)):
        for i in range(c+1, len(listA)):
            if listA[c] == 0 and listA[i] != 0:
                listA[c], listA[i] = listA[i], listA[c]
                break
list01=[0,2,4,0,5,0,0,2,0,6]
move_zero_bottom(list01)
print(list01)

#思想二：从后向前，如果发现零元素，删除并追加.
#1. 不能从前往后遍历，原因可以debug看
#2. 注意如何取的坐标
#3. del的用法要结合坐标使用，直接删除del item会报错
def zero_to_end(listB):
    for i in range(-1, -len(listB) - 1, -1):
        if listB[i] == 0:
            del listB[i]
            listB.append(0)
list02=[0,2,4,0,5,0,0,2,0,6]
zero_to_end(list02)
print(list02)