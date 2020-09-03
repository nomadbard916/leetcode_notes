from collections import Counter

#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)

        ans = []

        for num, count in counter.items():
            if count > n // 3:
                ans.append(num)

        return ans


# @lc code=end

