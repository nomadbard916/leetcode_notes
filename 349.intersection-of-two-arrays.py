#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []

        for num in nums1:
            if num in nums2:
                intersection.append(num)

        return list(set(intersection))


# @lc code=end

