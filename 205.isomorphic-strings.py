from collections import defaultdict

#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen_s_index = defaultdict(list)
        seen_t_index = defaultdict(list)

        for i, char in enumerate(s):
            seen_s_index[char].append(i)

        for i, char in enumerate(t):
            seen_t_index[char].append(i)

        s_i = list(seen_s_index.values())
        t_i = list(seen_t_index.values())

        return s_i == t_i


# @lc code=end

