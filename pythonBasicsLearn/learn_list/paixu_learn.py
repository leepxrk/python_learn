#!/usr/bin/python
# -*- coding: UTF-8 -*-



#列表函数
paixu = []

# paixu.append(33)  #在列表最后增加新的元素，一次仅能添加一个元素
# paixu.insert(0,68)   #insert方法有两个参数，第一个参数是代表函数插入的索引位，第二个参数代表插入的元素


#x = 1
#while x <= 5:
#    paixu.append(x)
#    print(x)
#    x += 1




y = len(paixu)

while y < 7:
    paixu.append(input("输入数值："))
    print(y)
    y = len(paixu)



paixu.sort()
print(paixu)
# print paixu