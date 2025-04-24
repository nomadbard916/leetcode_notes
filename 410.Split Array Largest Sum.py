#
# @lc app=leetcode id=410 lang=python3
# @lcpr version=30104
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # min-possible maximum => right bound
        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            tot, cnt = 0, 1
            for num in nums:
                if tot + num <= mid:
                    tot += num
                else:
                    tot = num
                    cnt += 1
            if cnt <= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi + 1  # Need to add 1 since hi points to value just below answer


# @lc code=end


#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#
