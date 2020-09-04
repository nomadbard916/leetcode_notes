#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if not prices:
            return max_profit

        for i, p in enumerate(prices):
            if i >= len(prices) - 1:
                break

            # keep buying and selling every day
            if prices[i + 1] > p:
                max_profit += prices[i + 1] - p

        return max_profit


# @lc code=end

