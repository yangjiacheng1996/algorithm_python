#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 选择算法原理：每次循环i加1，把i右边这一段(包括i)中的最小值放到i位置。
# 算法时间复杂度 bigO(N^2)
# 算法空间复杂度 bigO(1)
def selection_sort(array: list):
    if array is None or len(array) < 2:
        return array
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            min_index = j if array[j] < array[min_index] else min_index
        swap_list(array, i, min_index)
    return array


def swap_list(target_list: list, i: int, j: int):
    target_list[i], target_list[j] = target_list[j], target_list[i]


if __name__ == "__main__":
    a_list = [6, 2, 4, 5, 3, 1]
    b = selection_sort(a_list)
    print(b)
