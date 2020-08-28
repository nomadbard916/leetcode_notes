#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        numset = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in numset:
                ans.append(i)

        return ans


# @lc code=end

