#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        # initial state
        for i, c in enumerate(citations):
            # it is self evident.
            #  however time complexity O(n) is not fast enough
            if i >= c:
                return i

        return len(citations)

    # or can be done with binary search, see ref:
    #  https://blog.csdn.net/fuxuemingzhu/article/details/82949663
    # unsorted version of 275. H-Index II


# @lc code=end

