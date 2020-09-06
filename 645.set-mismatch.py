from collections import Counter

#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        ans = []

        for num, count in counter.items():
            if count == 2:
                ans.append(num)

        missing_num = set(range(1, len(nums) + 1)) - set(nums)

        ans.append(list(missing_num)[0])

        return ans


# @lc code=end

