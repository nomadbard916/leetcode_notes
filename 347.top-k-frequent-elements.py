#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # priority queue, aka. heap queue in python implementation
        counter = collections.Counter(nums)
        heap = []

        for num, count in counter.items():
            # priority takes order by first element of tuple counts[num]
            heapq.heappush(heap, (count, num))

            # always keep element count <= k with smallest popped first
            if len(heap) > k:
                heapq.heappop(heap)

        # turn heap to list, taking only num
        return [num for count, num in heap]






# @lc code=end

