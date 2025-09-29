#
# @lc app=leetcode id=239 lang=python3
# @lcpr version=30201
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        #  Deque stores indices of elements in decreasing order of their values
        dq = deque()
        res = []

        for i in range(len(nums)):
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


# @lc code=end


#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
