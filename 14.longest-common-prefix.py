#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # min() and max() implies "sorted",
        # i.e. anything in middle must have the common prefix,
        # so we only need to check these two
        min_str = min(strs)
        max_str = max(strs)

        for i, c in enumerate(min_str):
            if c != max_str[i]:
                return min_str[:i]

        return min_str


# @lc code=end
