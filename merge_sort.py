#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 归并排序原理：将一个无序列表通过不断地递归变成一个多叉树，然后从下往上不停地merge，最终实现一个有序列表。
# 比如列表是a = [6,2,4,5,3,1]，则process函数将这个a列表变成一个多叉树。
"""
                                        process(0,5)
                                        /         \
                                process(0,2)     process(3,5)
                            /         \               /         \
                    process(0,1)  process(2,2)   process(3,4)  process(5,5)
                  /      \                         /        \
        process(0,0)  process(1,1)         process(3,3)  process(4,4)

"""
# 由于迭代是一个堆栈的过程，计算机会从底往上计算多叉树，直至顶部的process(0,5) . 生产多叉树是从上往下，计算多叉树是从下往上。
# 所以需要一个merge函数，他的功能就是输入一个数组，并且规定好左端、中点、右端，然后将数组砍成两段，每次循环比较两段最左边的那个数。谁小就把谁加到临时数组中，然后指针右移。当两段中的某一段指针到达最右后，则直接将另一段剩余的数加入临时数组中。
# 由于process调用merge的顺序是多叉树自底向上的，所以运行过程中，merge所操作的数组一直是有序的。
# 算法时间复杂度bigO(NlogN)
# 算法空间复杂度bigO(N)
def merge_sort(array):
    process(array,0,len(array)-1)
    return array

def process(array, l, r):
    if l == r:
        return array
    if l < r:
        m = int((l + (r - 1)) / 2)
        process(array, l, m)
        process(array, m + 1, r)
        merge(array, l, m, r)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # 创建临时数组,制定数组长度，降低空间复杂度
    L = [0] * (n1)
    R = [0] * (n2)

    # 拷贝数据到临时数组 arrays L[] 和 R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # 归并临时数组到 arr[l..r]
    i = 0  # 初始化第一个子数组的索引
    j = 0  # 初始化第二个子数组的索引
    k = l  # 初始归并子数组的索引

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # 拷贝 L[] 的保留元素
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # 拷贝 R[] 的保留元素
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    a_list = [6, 2, 4, 5, 3, 1]
    b = merge_sort(a_list)
    print(b)
