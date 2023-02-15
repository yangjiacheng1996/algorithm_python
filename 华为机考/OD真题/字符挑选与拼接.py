#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
题目：
有A、B两个字符串，这两个字符串都是由[a-z]26个小写英文字母组成。其中A可能存在重复字母，B中不村子重复字母。现从字符串A中按规则挑选一些字母，
可以组成字符串B
1）同一个位置的字母只能被挑选一次
2）被挑选字母的相对信后顺序不能改变。
求最多可以同时从A中挑选多少组能组成B的字符串。

输入
0< A.length < 100
0< B.length < 10
'''
a = input()
b = input()
sum = 0
vis = [0] * len(a)
while True:
    #
    r = 0
    for i in range(len(a)):
        if vis[i] == 0 and r < len(b) and a[i] == b[r]:
            r += 1
            vis[i] = 1
    if r == len(b):
        sum += 1
    else:
        break
print(sum)

# 算法讲解：
'''
vis是A字符串的核对列表，如果A中的某个字符存在于B，则在vis中把这个字符在A中的位置标记一下，标记后，下一次循环就无法使用了
遍历B找A字符的过程是按照就近原则的，遍历成功，则sum+1并进行下一轮，遍历不成功，则break返回结果。遍历的过程中，如果vis位已经用过的，就跳过。
'''
