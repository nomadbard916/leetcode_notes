#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        LEN_S = len(s)
        longest = ""

        def findLongest(l: int, r: int):
            while l >= 0 and r < LEN_S and s[l] == s[r]:
                l -= 1
                r += 1
            # compensation
            return s[l + 1 : r]

        for i in range(LEN_S):
            # with single character in middle
            s1 = findLongest(i, i)
            if len(s1) > len(longest):
                longest = s1

            # with two characters in middle
            s2 = findLongest(i, i + 1)
            if len(s2) > len(longest):
                longest = s2

        return longest


# @lc code=end
