#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
题目：
给一个二维数组nums，对于每一个元素num[i]。找出距离最近且值相等的元素，输出横纵坐标差值的绝对值之和，如果没有等值元素，则输出-1.
例如：
输入数组nums为
0 3 5 4 2
2 5 7 8 3
2 5 4 2 4
对于num[0][0]，不存在相等的值
对于num[0][1] = 3，存在一个相等的值，最近的坐标为num[1][4]，最小距离是4。
对于num[0][2] = 5，存在两个相等的值，最近的坐标为num[1][1]，故最小距离是2。
对于num[1][1] = 5，存在两个相等的值，最近的坐标为num[2][1]，故最小距离为1。
...
故输出为
-1  4  2  3  3
 1  4 -1 -1  4
 1  1  2  3  2

输入：
输入第一行为二维数组的行
输入第二行为二维数组的列
输入的数字以空格隔开

输出：
数组形式返回所有坐标值。print(list)
'''


# 求最近元素的坐标之差的绝对值之和
def solve(n,m):
    dp = [0]*3005
    for i in range(1, n + 1):
        cnt = []
        for j in range(1, m + 1):
            mi = 1000005
            S1 = x[A[i][j]]
            S2 = y[A[i][j]]
            S = len(S1)
            for k in range(S):
                if (S1[k] != i or S2[k] != j):
                    s1 = abs(i - S1[k])
                    s2 = abs(j - S2[k])
                    mi = min(mi, s1 + s2)
            if (S == 1 and mi>=0):
                cnt.append(-1+dp[0])
            else:
                cnt.append(mi)
        dp[i] += mi
        list.append(cnt)


# 主程序
n = int(input())  # 行数
m = int(input())  # 列数
x = [[] for i in range(500005)]  # 相同数的的横坐标收集，x中元素的索引表示这个相同数
y = [[] for i in range(500005)]  # 相同数的的纵坐标坐标收集，x中元素的索引表示这个相同数
list = [] # 结果收集
A = [[0 for i in range(3005)] for i in range(3005)]  # 创建一个行列足够多的方阵。

for i in range(1, n + 1):
    s = input().split(' ')  # 接受num的每一行
    for j in range(1, m + 1):
        A[i][j] = int(s[j - 1])  # 将输入存入A中
        y[A[i][j]].append(j)  # 将每行的相同数字的纵坐标保存在y中，y中的index表示数，元素中保存这个数所有的纵坐标
        x[A[i][j]].append(i)  # 将每行的相同滋滋的横坐标保存在x中，x中的index表示数，元素中保存这个数所有的横坐标

solve(n,m)  # 将处理每个数的横纵坐标
print(list)
