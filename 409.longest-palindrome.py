#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # only one character
        if len(s) == 1:
            return 1

        # is palindrome itself
        if s == s[::-1]:
            return len(s)

        ans = 0
        for char_count in collections.Counter(s).values():
            # letters that can be paired, each pair add 2 to length
            ans += char_count // 2 * 2

            # character's count == 1 or is-odd
            char_might_be_unique = char_count % 2 == 1
            # not being added to ans yet means it IS the unique center
            uniq_char_not_added_yet = ans % 2 == 0

            if uniq_char_not_added_yet and char_might_be_unique:
                ans += 1

        return ans


# @lc code=end
