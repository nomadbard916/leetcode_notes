#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # sanity check
        if amount <= 0:
            return 0
        if min(coins) > amount:
            return -1

        # tabulation with $0 presented as 0 and others as infinity
        inf_int = 2 << 32
        table = [0] + [inf_int] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    table[i] = min((table[i - coin] + 1), table[i])

        return table[amount] if table[amount] != inf_int else -1


# @lc code=end

