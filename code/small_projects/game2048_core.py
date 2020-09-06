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


# 练习2：将相同数字合并（只合并一次）
# 　　[2,2,0,0]  --> [4,0,0,0]
#    [2,0,0,2]  --> [4,0,0,0]
#    [2,0,4,0]  --> [2,4,0,0]
#    [2,2,2,2]  --> [4,4,0,0]
#    [2,2,2,0]  --> [4,2,0,0]

#思想一：先遍历看有没有相同的，然后移动0
def combine_and_moveZero(listC):
    for i in range(len(listC)):
        for x in range(i+1, len(listC)):
            if listC[i] == listC[x]:
                listC[i] += listC[x]
                listC[x] = 0
                break
    move_back_zero(listC)
def move_back_zero(listD):
    for i in range(len(listD)):
        for x in range(i+1, len(listD)):
            if listD[i] == 0 and listD [x] != 0:
                listD[i], listD[x] = listD[x],listD[i]
                break
list03=[2,2,2,0]
combine_and_moveZero(list03)
print(list03)

#思想二：先移动0，后累加相同的数字
def move_to_back(listE):
    zero_to_end(listE)
    for i in range(len(listE)-1):
        if listE[i] == listE[i+1]:
            listE[i] += listE[i+1]
            del listE[i+1]
            listE.append(0)
list04 = [2,2,2,0]
move_to_back(list04)
print(list04)