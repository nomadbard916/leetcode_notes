from collections import defaultdict

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        # don't use ordinary dict as we need to initialize ad container to fill in
        sorted_strs_by_group_key = defaultdict(list)

        for str in strs:
            sorted_str = "".join(sorted(str))
            sorted_strs_by_group_key[sorted_str].append(str)

        for v in sorted_strs_by_group_key.values():
            ans.append(v)

        return ans


# @lc code=end
