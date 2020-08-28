from collections import Counter

#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        citems1 = c1.items()
        citems2 = c2.items()

        intersection = []

        for k1, v1 in citems1:
            if k1 in c2:
                intersection += [k1] * min(v1, c2[k1])

        return intersection


# @lc code=end

