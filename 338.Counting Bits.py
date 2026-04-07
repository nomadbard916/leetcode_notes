#
# @lc app=leetcode id=338 lang=python3
# @lcpr version=30305
#
# [338] Counting Bits
#

# @lc code=start
from __future__ import annotations

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # ! sol1: DP with lowest set bit
        # Key Insight:
        #   i & (i - 1)  →  removes the LOWEST set bit of i
        #   Example: i = 6  → binary 110
        #            i - 1 = 5  → binary 101
        #            6 & 5 = 100  → binary 100  (removed the lowest 1)
        #
        # So:  countBits[i] = countBits[i & (i - 1)] + 1
        #
        # Because i & (i-1) < i, we already have its answer in our dp array!
        #
        # Walk-through:
        #   i=0: 0b0000  → dp[0] = 0  (base case)
        #   i=1: 0b0001  → dp[1 & 0] + 1 = dp[0] + 1 = 1
        #   i=2: 0b0010  → dp[2 & 1] + 1 = dp[0] + 1 = 1
        #   i=3: 0b0011  → dp[3 & 2] + 1 = dp[2] + 1 = 2
        #   i=4: 0b0100  → dp[4 & 3] + 1 = dp[0] + 1 = 1
        #   i=5: 0b0101  → dp[5 & 4] + 1 = dp[4] + 1 = 2
        #   i=6: 0b0110  → dp[6 & 5] + 1 = dp[4] + 1 = 2
        #   i=7: 0b0111  → dp[7 & 6] + 1 = dp[6] + 1 = 3
        dp: List[int] = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i & (i - 1)] + 1

        return dp

        # ! sol2: DP with even/odd pattern
        # Observation:
        #   - Even number i: binary is just (i // 2) shifted left → same number of 1s
        #     e.g. 6 = 110, 3 = 11 → both have two 1s
        #   - Odd number i: one more 1 than i // 2
        #     e.g. 7 = 111, 3 = 11 → 7 has one more 1 than 3
        #
        # Recurrence:
        #   dp[i] = dp[i >> 1] + (i & 1)
        #           ↑ half of i   ↑ 1 if odd, 0 if even
        dp: List[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
            # i >> 1  is same as i // 2  (right-shift drops the last bit)
            # i & 1   is 1 if odd, 0 if even (checks the last bit)

        return dp

        # ! sol 3: Brute Force
        # For every number i, manually count its set bits.

        # bin(i) gives e.g. '0b1011', so we strip the prefix and count '1's.
        # Easy to understand, but not optimal.
        return [bin(i).count("1") for i in range(n + 1)]

        # * time & space complexity
        # Approach,Time Complexity,Space Complexity
        # Brute Force (bin().count),O(nlogn),O(n) for output
        # DP — Lowest Set Bit,O(n),O(n)
        # DP — Even/Odd,O(n),O(n)


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#
