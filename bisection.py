#!/usr/bin/env python
# -*- coding: utf-8 -*-

from insertion_sort import insertion_sort

# 二分法查找某个数。每次循环检查左端、右端、中点。（增加常数操作不影响算法的复杂度）
# 算法时间复杂度bigO(logN) , 即一个数组对半砍，砍几刀能砍完
# 算法空间复杂度bigO(1)
def bisection(array: list, find_num):
    insertion_sort(array)  # 先排一下序，随便用哪种排序方法
    if array == None or len(array) == 0:
        return False
    curser_left = 0  # 定义两个游标，一左一右
    curser_right = len(array) - 1  # 列表最后一位的index比列表长度小1
    while True:
        if array[curser_left] == find_num:
            return curser_left
        if array[curser_right] == find_num:
            return curser_right
        if curser_right - curser_left <= 1:
            break
        middle = curser_left + (
                    (curser_right - curser_left) >> 1)  # 相当于mid = int(l + (r-l)//2) , 但是位运算比整除快很多。这是算法高手求中点的固定写法，需要牢记！
        if find_num > array[middle]:
            curser_left = middle
        elif find_num < array[middle]:
            curser_right = middle
        else:  # 说明中点上的数就是我们要找的数，返回这个mid作为要找的数的index。如果遇到连续相同的数，不保证这个中点是连续最左端的index
            return middle
    return False


if __name__ == "__main__":
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(bisection(a_list,11))
