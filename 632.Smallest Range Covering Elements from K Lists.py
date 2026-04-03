#
# @lc app=leetcode id=632 lang=python3
# @lcpr version=30305
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start

import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        """
        * nouns and verbs
        sorted integers
        * pattern kws
        two pointers?
        * structure kws
        non-decreasing order, smallest range: one number from each of k list
        smaller rule:  range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c
        * map kws to algo
        * mental model
        * tricky kws
        1<=k<=3500 and 1<=len<=50, total 165000 => cannot brute force
        * pattern specific kws
        """
        # * take the smallest and biggest, and shrink? is this greedy?
        # like backtracking, take numbers and unmake choice?
        # record (val, list, idx) in heap?

        # how do I determine if a num from list is within range?
        # start from first element and go all the way down?
        # keep updating range?
        # can I use heap for each list?
        # make the range first anyway?

        # visualize the overlapping first
        res_range = [float("-inf"), float("inf")]

        curr_max: float | int = float("-inf")
        # for each heap item: (value, list_index, elem_index)
        min_heap: list[tuple[int, int, int]] = []

        for list_idx, sorted_list in enumerate(nums):
            curr_val = sorted_list[0]
            heapq.heappush(min_heap, (curr_val, list_idx, 0))
            curr_max = max(curr_max, curr_val)

        while min_heap:
            curr_min, list_idx, elem_idx = heapq.heappop(min_heap)

            if curr_max - curr_min < res_range[1] - res_range[0]:
                res_range = [curr_min, curr_max]

            next_elem_idx = elem_idx + 1
            if next_elem_idx >= len(nums[list_idx]):
                break

            next_val = nums[list_idx][next_elem_idx]
            heapq.heappush(min_heap, (next_val, list_idx, next_elem_idx))
            curr_max = max(curr_max, next_val)

        return res_range  # ty:ignore[invalid-return-type]


# @lc code=end


#
# @lcpr case=start
# [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#
