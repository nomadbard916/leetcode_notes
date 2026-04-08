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

        # So your instinct — "find the number that has exactly one fewer 1, and build from there" — is exactly right.
        # The key question is just: how do you reliably find that number?
        # That's what i & (i-1) does. It doesn't go to i-1 in decimal.
        # Instead it surgically removes the lowest set bit of i, giving you a number that:
        # - is guaranteed to have exactly one fewer 1 than i
        # - is guaranteed to be < i, so it's already computed in our DP table

        # So the full restatement of the insight in your own words:
        # "For any number i, find the number that has exactly one fewer 1-bit — that's i & (i-1) — and just add 1."
        # That's precisely dp[i] = dp[i & (i-1)] + 1.
        # You had the right idea, just needed the right tool to find that "one less" number reliably. 🎯
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
        #         decimal   binary    last bit    odd/even?
        # ──────────────────────────────────────────
        # 0       0000         0          even
        # 1       0001         1          odd
        # 2       0010         0          even
        # 3       0011         1          odd
        # 4       0100         0          even
        # 5       0101         1          odd
        # 6       0110         0          even
        # 7       0111         1          odd

        # Why Does & 1 Extract the Last Bit?
        # 1 in binary is 0001 — it has a 1 only in the last position, and 0 everywhere else.
        # AND (&) works bit by bit: 1 & 1 = 1, and anything & 0 = 0.
        # So i & 1 masks out every bit except the last one:
        # 6  =  ...0110
        # 1  =  ...0001
        #         ──────  AND
        #         ...0000  →  0  (even ✅)

        # 7  =  ...0111
        # 1  =  ...0001
        #         ──────  AND
        #         ...0001  →  1  (odd ✅)
        # All the upper bits get zeroed out. Only the last bit survives. That's all & 1 does — it's a bit mask that isolates position 0.
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
        # A number `i` in binary has exactly **⌊log₂(i)⌋ + 1** digits, so it's O(log n)
        # ```
        # i = 1   →  "1"       →  1 digit   (log₂(1) = 0)
        # i = 2   →  "10"      →  2 digits  (log₂(2) = 1)
        # i = 4   →  "100"     →  3 digits  (log₂(4) = 2)
        # i = 8   →  "1000"    →  4 digits  (log₂(8) = 3)
        # i = 16  →  "10000"   →  5 digits  (log₂(16) = 4)
        # ```
        # # and repeating n times gives O(n log n)
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
