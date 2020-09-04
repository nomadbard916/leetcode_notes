#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        if not nums:
            return ans

        slow = 0

        while slow < len(nums):
            # start range searching
            fast = slow

            # find incrementing value
            while fast < len(nums) - 1 and nums[fast] + 1 == nums[fast + 1]:
                fast += 1

            # only 1, ie previous while is not moving fast pointer
            if fast == slow:
                ans.append(str(nums[slow]))
            # has range
            else:
                start = str(nums[slow])
                end = str(nums[fast])

                ans.append(f"{start}->{end}")

            slow = fast + 1

        return ans


# @lc code=end

