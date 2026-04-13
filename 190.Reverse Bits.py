#
# @lc app=leetcode id=190 lang=python3
# @lcpr version=30305
#
# [190] Reverse Bits
#

# @lc code=start
from __future__ import annotations


class Solution:
    def reverseBits(self, n: int) -> int:
        # ! sol1 : Bit-by-bit streaming  (O(32) = O(1) time, O(1) space)
        # Intuition:
        #   Each iteration we "peel" the least significant bit (LSB) from n,
        #   then OR it into the result after shifting result left by 1.
        #   After 32 iterations, the LSB of the original n sits at bit 31 of result.
        #
        # Loop body breakdown:
        #   result = (result << 1) | (n & 1)
        #     ^          ^                ^
        #     |          |                └── extract LSB of n
        #     |          └─ make room on the right of result
        #     └─ OR in the extracted bit
        #   n >>= 1   ← discard the bit we just used
        #
        # Why 32 iterations exactly?
        #   We want to cover all 32 bit positions regardless of how many leading zeros
        #   the input has. If n becomes 0 early, we still shift result left, which
        #   correctly pads zeros into the remaining positions.
        result = 0
        for _ in range(32):
            # 1. make room with a 0 on the right for result
            # 2. extract the least significant bit
            # 3. use OR to attach anything of LSB onto result anyway
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

        # ! sol 2: Explicit positional placement  (O(32) = O(1) time, O(1) space)
        # Intuition:
        #   More explicit version. At iteration i (0-indexed from LSB),
        #   bit i of n goes to bit (31 - i) of result.
        #   We extract it with (n >> i) & 1, then shift it into place.
        #
        # This is mathematically identical to Approach 1, but written to make the
        # "mirror position" invariant explicit: bit_i → bit_(31-i).

        result: int = 0
        for i in range(32):
            bit: int = (n >> i) & 1  # extract bit at position i
            result |= bit << (31 - i)  # place it at mirror position 31-i
        return result


# @lc code=end


#
# @lcpr case=start
# 43261596\n
# @lcpr case=end

# @lcpr case=start
# 2147483644\n
# @lcpr case=end

#
