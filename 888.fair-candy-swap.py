#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # SA−x+y=SB−y+x
        # -> y = x + (SB-SA) //2
        sumA, sumB = sum(A), sum(B)
        setB = set(B)

        for x in A:
            if x + (sumB - sumA) // 2 in setB:
                return [x, x + (sumB - sumA) // 2]


# @lc code=end

