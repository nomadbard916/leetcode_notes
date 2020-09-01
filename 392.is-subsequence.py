from collections import deque

#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # keep relative positions: use queue or stack

        queue = deque(s)

        for char in t:
            if len(queue) == 0:
                return True

            if char == queue[0]:
                queue.popleft()

        return len(queue) == 0


# @lc code=end

