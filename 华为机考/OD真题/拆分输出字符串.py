#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
连续输入字符串（输出次数为N，字符串长度小于100），请按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
'''
import sys

lines = [line.rstrip() for line in sys.stdin]


def split_by_len(a: str, n: int):
    results = []
    while True:
        if len(a)==0:
            break
        elif len(a) <= n:
            a = a + "0" * (n - len(a))
            results.append(a)
            break
        else:
            results.append(a[:n])
            a = a[n:]
    return results


source_string = lines[0]
if len(source_string) > 0:
    results = split_by_len(source_string, 8)
    for r in results:
        print(r)