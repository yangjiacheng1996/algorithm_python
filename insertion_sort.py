#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 插入排序原理：i是指针，从1开始迭代i++，每次循环都要确保i-1位小于i位。如果i-1位>i位，则执行一个遍历，逆向冒泡将数插入到合适的位置。插入排序全过程类似打扑克时抓牌码牌过程。
# 算法时间复杂度bigO(N^2)
# 算法空间复杂度bigO(1)
def insertion_sort(array: list):
    if array is None or len(array) < 2:
        return array
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] > array[j + 1]:
                swap_list(array, j, j + 1)
    return array


def swap_list(target_list: list, i: int, j: int):
    target_list[i], target_list[j] = target_list[j], target_list[i]


if __name__ == "__main__":
    a_list = [6, 2, 4, 5, 3, 1]
    b = insertion_sort(a_list)
    print(b)
