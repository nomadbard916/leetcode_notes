#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Related Problems to Practice:
        # 0/1 Knapsack: True "take or don't take" each item once
        # Combination Sum: Like coin change but return all combinations
        # Word Break: Can you form a word using dictionary words?

        # ! sol1: DP

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
                    DP[curr_amount] = min(
                        # 1. Current value, don't take the new one
                        DP[curr_amount],
                        # 2. Using this coin (+1) + minimum coins for remaining amount
                        DP[curr_amount - coin] + 1,
                    )

        if DP[amount] == IMPOSSIBLE_VALUE:
            return -1

        return DP[amount]

        # Time Complexity: O(amount × number of coins)
        # We iterate through each amount from 1 to amount
        # For each amount, we try all coin denominations

        # Space Complexity: O(amount)
        # We use a dp array of size amount + 1

        # ! sol2: DFS with memo
        # actually you should think of DFS first

        memo = {}

        def dfs(remaining_amount: int) -> int:
            # Check memo first!
            if remaining_amount in memo:
                return memo[remaining_amount]

            # Base cases (same as pure DFS)
            if remaining_amount == 0:
                return 0
            if remaining_amount < 0:
                return float("inf")

            min_coins = float("inf")

            # Same loop structure as DFS and bottom-up DP!
            for coin in coins:
                if coin <= remaining_amount:
                    result = dfs(remaining_amount - coin)
                    if result != float("inf"):
                        min_coins = min(min_coins, result + 1)

            # Store result in memo before returning
            memo[remaining_amount] = min_coins
            return min_coins

        result = dfs(amount)
        return result if result != float("inf") else -1


# @lc code=end
