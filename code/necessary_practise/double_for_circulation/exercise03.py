"""
无序列表[3, 80, 45, 5, 7, 1] 按大小排序
# 目标:列表中所有元素两两比较
# 思想:
# 　取出第一个元素,与后面元素进行比较.
# 　取出第二个元素,与后面元素进行比较.
# 　取出第三个元素,与后面元素进行比较.
#   ...
#   取出倒数第二个元素,与后面元素进行比较.
#   如果取出的元素大于(>)后面的元素,
#       则交换
"""
#法一：
list01 = [3, 80, 45, 5, 7, 9]
for i in range(len(list01)):
    for j in range(i, len(list01)):
        if (list01[i] > list01[j]):
            temp = list01[i]
            list01[i] = list01[j]
            list01[j] = temp
print(list01)

#法二：
list02 = [3, 80, 45, 5, 7, 9]
for r in range(len(list02) - 1):
    for c in range(r+1, len(list02)):
        if list02[r] < list02[c]:
            list02[r], list02[c] = list02[c], list02[r]
print(list02)
