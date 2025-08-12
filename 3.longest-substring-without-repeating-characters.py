#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set initial length = 0
        # return length: int

        # sliding window

        # how to determine next position when the temp result is found?

        seen_char_pos: Dict[str, int] = {}

        l = 0
        r = 0

        max_length = 0
        n = len(s)

        while l < n and r < n and l <= r:
            current_c = s[r]

            if current_c in seen_char_pos:
                # a new string must exclude previously seen character
                l = max(l, seen_char_pos[current_c] + 1)

            seen_char_pos[current_c] = r

            max_length = max(max_length, r - l + 1)

            r += 1

        return max_length


# @lc code=end
