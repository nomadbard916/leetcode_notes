#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap: tuple[int, int] = []

        for num, count in counter.items():
            # priority takes order by first element of tuple (count, num)
            # if count cannot be compared i.e. duplication, num is compared next
            heappush(heap, (count, num))

            # always keep element count <= k with smallest popped first
            if len(heap) > k:
                heappop(heap)

        # turn heap to list, taking only num
        return [num for _, num in heap]


# @lc code=end
