#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 冒泡排序原理：i是指针，起始点是0，终点是end，每次i右移的时候都会检查i和i+1位哪个大，如果i比i+1位大，则进行交换。这样通过频繁的交换，列表中最大的数不断右移直到end位置。第一轮循环后最大的数就放到最右边。然后终点end-1，进行第二轮冒泡，以此类推。
# 算法时间复杂度bigO(N^2)
# 算法空间复杂度bigO(1)
def bubble_sort(array: list):
    if array is None or len(array) < 2:
        return array
    for end in range(len(array) - 1, 0, -1):
        for i in range(end):
            if array[i] > array[i + 1]:
                swap_list(array, i, i + 1)
    return array


def swap_list(target_list: list, i: int, j: int):
    target_list[i], target_list[j] = target_list[j], target_list[i]


if __name__ == "__main__":
    a_list = [6, 2, 4, 5, 3, 1]
    b = bubble_sort(a_list)
    print(b)
