#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sanity check
        if amount <= 0:
            return 0
        if min(coins) > amount:
            return -1

        # just make it a little bigger to be impossible, instead of INF
        IMPOSSIBLE_VALUE = amount + 1

        # dp[i] represents the minimum coins needed to make amount i
        # Initialize with amount + 1 (impossible value) except dp[0] = 0
        DP = [IMPOSSIBLE_VALUE] * (amount + 1)
        DP[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                # If this coin can be used (doesn't exceed current amount)
                if coin <= curr_amount:
                    # Update dp[current_amount] with minimum of:
                    # 1. Current value
                    # 2. Using this coin + minimum coins for remaining amount
                    DP[curr_amount] = min((DP[curr_amount - coin] + 1), DP[curr_amount])

        if DP[amount] == IMPOSSIBLE_VALUE:
            return -1

        return DP[amount]


# @lc code=end
