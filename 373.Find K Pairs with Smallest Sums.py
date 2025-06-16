#
# @lc app=leetcode id=373 lang=python3
# @lcpr version=30104
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq
import itertools
from queue import PriorityQueue
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # ! sol1
        # * it's essentially the extension of # 23 "merge k sorted lists"
        # think of the input as an m x n matrix,
        # for example for nums1=[1,7,11], and nums2=[2,4,6]:
        #       2   4   6
        #    +------------
        #  1 |  3   5   7
        #  7 |  9  11  13
        # 11 | 13  15  17
        # Of course the smallest pair overall is in the top left corner, the one with sum 3.
        # We don't even need to look anywhere else. After including that pair in the output,
        # the next-smaller pair must be the next on the right (sum=5) or the next below (sum=9).
        # We can keep a "horizon" of possible candidates, implemented as a heap / priority-queue,
        # and roughly speaking we'll grow from the top left corner towards the right/bottom.
        # PriorityQueue used here as there are some convenient functionalities like empty()
        pq = PriorityQueue()

        # init pq
        nums1_first_idx = 0
        for i in range(len(nums2)):
            # just put in some smaller ones,
            # as nums1[i] + nums2[0] must be the smallest from nums1 side
            pq.put(
                (
                    nums1[nums1_first_idx] + nums2[i],
                    nums1[nums1_first_idx],
                    nums2[i],
                    nums1_first_idx,
                )
            )

        res = []

        # * merge multiple sorted lists
        while not pq.empty() and k > 0:
            _, num1, num2, curr_idx = pq.get()
            k -= 1
            # put smaller nodes into pq from nums2 side
            next_idx = curr_idx + 1
            if next_idx < len(nums1):
                pq.put((nums1[next_idx] + num2, nums1[next_idx], num2, next_idx))

            # just append pairs so their sum is guaranteed to be ascending from min
            pair = [num1, num2]
            res.append(pair)

        return res

        # ! sol2: brute force
        return sorted(itertools.product(nums1, nums2), key=sum)[:k]
        # it should be cleaner with list to be:
        # return map(list, sorted(itertools.product(nums1, nums2), key=sum)[:k])

        # ! sol3: Less Brute Force, with help from heapq.nsmallest()
        return map(list, heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum))

        # ! sol4: just push everything into heapq and do comparison
        queue = []

        def push(i: int, j: int):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

        push(0, 0)

        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i] + nums2[j], i, j])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)

        return pairs


# @lc code=end


#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#
