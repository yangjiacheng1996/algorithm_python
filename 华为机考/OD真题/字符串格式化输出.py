#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
输入形如AB-ABC-cABd-Cb@的字符串，输入待分割长度k。
要求输出保留第一个“-”前面的字符串格式，后面的每k个字符一分格
每三个字符中，大写字母数多的三个字符转大写，小写字母数多的三个字符转小写，一样多的不处理。
'''
import sys

'''
输入：
AB-ABC-cABd-Cb@
2

输出：
AB-AB-CC-AB-dc-b@
'''


def alpha_continent(s:str):
    alpha_cache= []
    s_list= list(s)
    for c in s_list:
        if str(c).isalpha():
            alpha_cache.append(c)
    lower_alpha = 0
    upper_alpha = 0
    for a in alpha_cache:
        if str(a).islower():
            lower_alpha += 1
        else:
            upper_alpha += 1
    if lower_alpha > upper_alpha:
        return s.lower()
    elif lower_alpha < upper_alpha:
        return s.upper()
    else:
        return s

def continent_by_length(s:str,l:int):
    result = []
    while True:
        if len(s) == 0:
            break
        elif len(s)<l:
            result.append(alpha_continent(s))
            break
        else:
            result.append(alpha_continent(s[:l]))
            s = s[l:]
    return "".join(result)



def connect_by_length(s:str,k:int):
    result = []
    while True:
        if len(s) == 0:
            break
        elif len(s)<k:
            result.append(s)
            break
        else:
            result.append(s[:k])
            s = s[k:]
    return "-".join(result)

def main():
    while True:
        try:
            s = input()
            k = int(input())
            groups = s.split("-")
            head, tail = groups[0], "".join(groups[1:])
            tail = continent_by_length(tail,3)
            print(head + "-" + connect_by_length(tail, k))
        except Exception as e:
            print(e)
            print("input error")
if __name__ == "__main__":
    main()
