#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
选择排序：
它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
存放在序列的起始位置，所以称为：选择排序。

时间复杂度： O(n^2)
空间复杂度： O(1)
"""

from Utils.timer_decorater import timer
from typing import List


class Solution:
    @timer
    def selection_sort(self, l: List) -> List:
        if len(l) <= 1:
            return l

        # for index in range(len(l)):
        #     min_index = index
        #     for j in range(index + 1, len(l)):
        #         if l[j] < l[min_index]:
        #             min_index = j
        #
        #     l[index], l[min_index] = l[min_index], l[index]
        for index in range(len(l) - 1):
            max_index = index
            for j in range(index + 1, len(l)):
                if l[j] > l[max_index]:
                    max_index = j

            l[index], l[max_index] = l[max_index], l[index]

        return l


if __name__ == "__main__":
    need_sort_list = [2, 4, 8, 1, 7, 10, 12, 15, 3]
    print(Solution().selection_sort(need_sort_list))
