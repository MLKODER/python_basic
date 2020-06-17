"""
外层循环控制行，内层循环控制列
打出
*#*#*#
*#*#*#
*#*#*#
*#*#*#
"""
for r in range(4):
    for t in range(6):
        if t % 2 == 0:
            print("*", end = "")
        else:
            print("#", end = "")
    print()