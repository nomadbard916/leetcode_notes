#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        bought_price = float("INF")

        for p in prices:
            if p < bought_price:
                bought_price = p
            else:
                current_profit = max(current_profit, p - bought_price)

        return current_profit


# @lc code=end

