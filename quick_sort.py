#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


# 快排1.0版原理：根据荷兰国旗算法，以数组最右边的数为num，将其余数分成小于等于区和大于区两段。然后将最后的num与大于区的第一个进行交换（[j]与[-1]）
# num到达位置后认为已经排好，然后对小于区和大于区继续进行如上操作，将小于区的最后一位作为num进行二段分，大于区也二段分，这样无限递归下去，就变成了有序数组。
# 每次递归的时候从事保证num被排好，无限递归后变成有序。

# 快排2.0版原理：原理类似1.0版，以数组最右边数作为num进行三段荷兰国旗算法，与num相等的区域认为已经排好。
# 相比1.0每次只排一个，2.0版每次排一批数，所以速度比1.0高。所以快排算法直接把荷兰国旗算法拿来套一个主函数进行递归就行了。
# 快排2.0的时间复杂度是N^2的，原因是num值的划分太偏了，导致左段和右端的长度不行等。算法从NlogN退化到N^2

# 快排3.0，为了保证每次递归是小于区和大于区长度基本一致，需要这个num随机抽取然后放到数组的最后。
# 由于这个算法单次运行的效果时好时差，但是长期的数学期望是num在中点处，所以这个算法就是NlogN算法。


def quick_sort(array: list):
    process(array, 0, len(array) - 1)
    return array


def process(array: list, L, R):
    if L < R:
        swap_list(array, L + int(random.random()) * (R - L + 1), R)
        p = partition(array, L, R)
        process(array, L, p[0] - 1)
        process(array, p[1] + 1, R)


def partition(array, L, R):
    less = L - 1  # 小于区边界的index
    more = R  # 大于区边界的index
    while L < more:
        if array[L] < array[R]:
            less += 1
            swap_list(array, less, L)
            L += 1
        elif array[L] > array[R]:
            more -= 1
            swap_list(array, more, L)
        else:
            L += 1
    swap_list(array, more, R)
    return [less + 1, more]


def swap_list(target_list: list, i: int, j: int):
    target_list[i], target_list[j] = target_list[j], target_list[i]


if __name__ == "__main__":
    a_list = [6, 2, 4, 5, 3, 1, 9, 111]
    b = quick_sort(a_list)
    print(b)
