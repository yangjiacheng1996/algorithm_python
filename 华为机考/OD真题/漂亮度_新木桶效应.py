#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
给出一个字符串，该字符串仅由小写字母组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个不同字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个字符串，计算每个字符串最大可能的“漂亮度”。
数据范围：输入的名字长度满足 1≤n≤10000

输入：
2
zhangsan
lisi

输出：
192
101
说明：对于样例lisi，让i的漂亮度为26，l的漂亮度为25，s的漂亮度为24，lisi的漂亮度为25+26+24+26=101.

'''
n = int(input())
for i in range(n):
    target = input()
    str_list = list(target.strip())
    a = set(str_list)
    alpha_times = {}
    for c in a:
        sum = 0
        for d in str_list:
            if c == d:
                sum += 1
        alpha_times[c] = sum
    chongfu = [v for v in alpha_times.values()]
    chongfu.sort(reverse=True)
    first_p = 26
    for c in chongfu:
        for k, v in alpha_times.items():
            if v == c:
                alpha_times[k] = first_p
                first_p -= 1
    result = 0
    for c in str_list:
        try:
            result += alpha_times[c]
        except Exception as e:
            print("error, char piaoliang not known")
    print(result)
