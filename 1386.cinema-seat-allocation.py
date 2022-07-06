#
# @lc app=leetcode id=1386 lang=python3
#
# [1386] Cinema Seat Allocation
#

# @lc code=start
import collections
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # the only feasible allocations:
        # [2,5], [6,9], [4,7], [2..9]

        # use "set" here as we'll use 'intersect' later
        occupied_row_nums_map = collections.defaultdict(set)
        for row, num in reservedSeats:
            occupied_row_nums_map[row].add(num)

        occupied_row_available_groups = 0

        alloc_all = set(range(2, 10))
        alloc_1 = set(range(2, 6))
        alloc_2 = set(range(4, 8))
        alloc_3 = set(range(6, 10))

        for occupied_nums in occupied_row_nums_map.values():
            if len(occupied_nums & alloc_all) == 0:
                occupied_row_available_groups += 2
            elif (
                len(occupied_nums & alloc_1) == 0
                or len(occupied_nums & alloc_2) == 0
                or len(occupied_nums & alloc_3) == 0
            ):
                occupied_row_available_groups += 1

        empty_row_available_groups = (n - len(occupied_row_nums_map)) * 2

        return occupied_row_available_groups + empty_row_available_groups


# @lc code=end
