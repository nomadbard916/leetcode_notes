#
# @lc app=leetcode id=373 lang=python3
# @lcpr version=30104
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
from queue import PriorityQueue
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        # * it's essentially the extension of # 23 "merge k sorted lists"
        # priority queue is used here as there are some convenient functionalities like empty()
        pq = PriorityQueue()

        # init pq
        res_first_idx = 0
        for i in range(len(nums1)):
            # just put in some smaller ones,
            # as nums1[i] + nums2[0] must be the smallest from nums1 side
            pq.put(
                (
                    nums1[i] + nums2[res_first_idx],
                    nums1[i],
                    nums2[res_first_idx],
                    res_first_idx,
                )
            )

        res = []

        # * merge multiple sorted lists
        while not pq.empty() and k > 0:
            _, num1, num2, curr_idx = pq.get()
            k -= 1
            # put smaller nodes into pq from nums2 side
            next_idx = curr_idx + 1
            if next_idx < len(nums2):
                pq.put((num1 + nums2[next_idx], num1, nums2[next_idx], next_idx))

            # just append pairs so their some is guaranteed to be ascending from min
            pair = [num1, num2]
            res.append(pair)

        return res


# @lc code=end


#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#
