#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True

        insensitive = s.lower()
        puncless_string_container = []

        for s in insensitive:
            if s.isalnum():
                puncless_string_container.append(s)

        puncless = "".join(puncless_string_container)

        return puncless == puncless[::-1]

        # cleanlist = [c for c in s.lower() if c.isalnum()]
        # return cleanlist == cleanlist[::-1]


# @lc code=end

