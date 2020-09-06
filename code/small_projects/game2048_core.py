"""
2048  游戏核心算法
"""
# 练习１：零元素移至末尾
# 　　[2,0,2,0]  --> [2,2,0,0]
#    [2,0,0,2]  --> [2,2,0,0]
#    [2,4,0,2]  --> [2,4,2,0]
def move_zero_bottom(listA):
    for c in range(len(listA)):
        for i in range(-1, -(len(listA)-c),-1):
            if listA[c] == 0 and listA[i] != 0:
                listA[c], listA[i] = listA[i], listA[c]
                break
list01=[2,4,0,2]
move_zero_bottom(list01)
print(list01)