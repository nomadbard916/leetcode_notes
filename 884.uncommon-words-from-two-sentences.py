from collections import Counter

#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        cA = Counter(A.split())
        cB = Counter(B.split())

        AB_counter = cA + cB

        return [word for word in AB_counter if AB_counter[word] == 1]


# @lc code=end

