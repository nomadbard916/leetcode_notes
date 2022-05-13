#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        left, right = 0, 0
        ans = 0

        # counting appearance times for each character in window
        char_counter = Counter()

        while right < len(s):
            char_r = s[right]
            char_counter[char_r] += 1

            right += 1

            # move left,
            # while every char count other than dominant cannot be greater than k
            # right - left don't need plus one as right has already moved
            while right - left - max(char_counter.values()) > k:
                char_l = s[left]
                char_counter[char_l] -= 1

                left += 1

            ans = max(ans, right - left)

        return ans


# @lc code=end
