from collections import defaultdict

#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:

        m = defaultdict(int)  # defaults 0
        ans = 0

        # group them two by two and sum them, then record in hash map
        for na in A:
            for nb in B:
                ab_sum = na + nb
                m[ab_sum] += 1

        # find complement sum in m from previous group of two
        for nc in C:
            for nd in D:
                target = -(nc + nd)

                if target in m:
                    ans += m[target]

        return ans


# @lc code=end

