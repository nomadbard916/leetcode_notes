#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)

        # if needle is "": return 0
        # if len(needle) > len(haystack): return -1

        # iterate over needle:
        # iterate over haystack
        # if iterated needle element == haystack element, keep iterating until reaching one of the end

        # return -1 if one of the above conditions is not satisfied

        # two pointer?

        ln = len(needle)
        lh = len(haystack)

        if needle == "":
            return 0

        if ln > lh:
            return -1

        for i in range(lh - ln + 1):
            if haystack[i : i + ln] == needle:
                return i

        return -1


# @lc code=end

