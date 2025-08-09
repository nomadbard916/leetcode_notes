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

        DP = [amount + 1] * (amount + 1)
        DP[0] = 0

        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    DP[curr_amount] = min((DP[curr_amount - coin] + 1), DP[curr_amount])

        if DP[amount] == amount + 1:
            return -1

        return DP[amount]


# @lc code=end
