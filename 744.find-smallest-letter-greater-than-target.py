#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()

        for l in letters:
            if l > target:
                return l

        return letters[0]


# @lc code=end

