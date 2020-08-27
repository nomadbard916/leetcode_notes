#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        exploded = s.split()

        return len(exploded[-1]) if len(exploded) >= 1 else 0


# @lc code=end

