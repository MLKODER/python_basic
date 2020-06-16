"""
随即输入一个字符串，并统计出每个字符出现的次数
比如aidofjs
"""
str_list = {}
str_random = input("请输入一个字符串：")
for item in str_random:
    if item in str_list:
        str_list[item] += 1
    elif item not in str_list:
        str_list[item] = 1
    # str_list[item]=count
print(str_list)