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
        k sorted integers, range[a, b]
        find, cover, includes (at least one from each list), minimize
        * pattern kws
        two pointers?
        smallest range -> sliding window or greedy
        k sorted lists -> merge k lists, heap/priority queue
        at least one from each -> coverage constrain
        * structure kws
        sorted: order can be exploited
        non-decreasing order, smallest range: one number from each of k list
        smaller rule:  range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c
        * map kws to algo
        k sorted lists => min-heap for merge
        smallest range => track current min & max in heap
        at least one from each => maintain exactly k representatives
        minimize b-a => greedy: advance the min element

        * mental model
        heap: we can always know the current minimum
        track global max: as heap gives min, we need to track max ourselves
        sliding window across sorted merge -> advance pointer of the list owning the current min
        * tricky kws
        1<=k<=3500 and 1<=len<=50, total 165000 => cannot brute force
        smallest range
        * pattern specific kws
        """

        """
        thoughts process
        # take the smallest and biggest, and shrink? is this greedy?
        # like backtracking, take numbers and unmake choice?
        # record (val, list, idx) in heap?

        # how do I determine if a num from list is within range?
        # start from first element and go all the way down?
        # keep updating range?
        # can I use heap for each list?
        # make the range first anyway?

        # visualize the overlapping first
        """

        # ! LC 632 = LC 76 (Minimum Window Substring) applied to k sorted lists,
        # where the heap replaces the explicit merge + sort step and saves memory.

        # * as the range keeps changing, just keep them floating with impossibly wide range
        res_range = [float("-inf"), float("inf")]

        # * init the heap with the first and smallest element of each list
        curr_max: float | int = float("-inf")
        # for each heap item: (value, list_index, elem_index)
        min_heap: list[tuple[int, int, int]] = []

        for list_idx, sorted_list in enumerate(nums):
            curr_val = sorted_list[0]
            heapq.heappush(min_heap, (curr_val, list_idx, 0))
            curr_max = max(curr_max, curr_val)

        # * greedy loop
        while min_heap:
            curr_min, list_idx, elem_idx = heapq.heappop(min_heap)

            # update answer if current window is smaller
            if curr_max - curr_min < res_range[1] - res_range[0]:
                res_range = [curr_min, curr_max]

            # Try to advance: push the NEXT element from the same list
            next_elem_idx = elem_idx + 1
            curr_list = nums[list_idx]
            # out of bound: This list is exhausted → we can no longer cover all lists → stop, early return
            if next_elem_idx >= len(curr_list):
                break

            next_val = curr_list[next_elem_idx]
            heapq.heappush(min_heap, (next_val, list_idx, next_elem_idx))

            curr_max = max(curr_max, next_val)

        return res_range  # ty:ignore[invalid-return-type]

        # complexities
        # Time O(N log k) where N = total elements across all lists, log k for each heap operation
        # Space O(k) — the heap holds exactly k elements at any time

        # why not use max heap and track min?
        # The Fundamental Asymmetry:
        # The lists are sorted ascending. So:
        # - Advancing a list → next element is larger or equal
        # - We want to raise the floor (min) → must advance the min-owner ✅
        # - Advancing the max-owner → next element even larger → widens range ❌
        # This means the algorithm is inherently min-first. The min is the one that needs to move, so you need O(log k) access to the min and its identity — which is exactly what a min-heap gives you.


# @lc code=end


#
# @lcpr case=start
# [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[1,2,3],[1,2,3]]\n
# @lcpr case=end

#
