from collections import defaultdict

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import Collection


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        # sorted_strs = {}
        sorted_strs = defaultdict(list)

        for s in strs:
            sorted_str = "".join(sorted(s))

            # if sorted_str not in sorted_strs:
            #     sorted_strs[sorted_str] = []

            # sorted_strs[sorted_str].append(s)

            sorted_strs[sorted_str].append(s)

        for v in sorted_strs.values():
            ans.append(v)

        return ans


# @lc code=end

