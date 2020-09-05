#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # remove character on left or on right
                l_string, r_string = (s[:l] + s[l + 1 :], s[:r] + s[r + 1 :])

                return l_string == l_string[::-1] or r_string == r_string[::-1]
            l += 1
            r -= 1
        return True


# @lc code=end

