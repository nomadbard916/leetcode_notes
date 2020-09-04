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

        for current_p in prices:
            bought_price = min(current_p, bought_price)

            current_profit = max(current_profit, current_p - bought_price)

        return current_profit


# @lc code=end

