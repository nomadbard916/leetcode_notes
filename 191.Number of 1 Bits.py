#
# @lc app=leetcode id=191 lang=python3
# @lcpr version=30305
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        # !sol1
        # The whole process looks like this:
        # Think about all the digits of this number being on a belt, one by one.
        # We are checking the rightmost element,
        # and the elements are going right one by one until we check the leftmost element.
        """
        Check each bit one by one from LSB to MSB.

        Technique:
            - `n & 1`  → extract the last (least significant) bit
            - `n >>= 1` → shift all bits one position to the right (drop the last bit)

        Visualised for n = 13  (binary: 1101)
            Step 1: 1101 & 0001 = 1  → count = 1,  n = 0110
            Step 2: 0110 & 0001 = 0  → count = 1,  n = 0011
            Step 3: 0011 & 0001 = 1  → count = 2,  n = 0001
            Step 4: 0001 & 0001 = 1  → count = 3,  n = 0000
            … remaining 28 shifts all yield 0

        We run exactly 32 iterations to cover a 32-bit integer.
        """
        count = 0
        for _ in range(32):
            # add 1 if last bit is set, else add 0
            count += n & 1
            # unsigned right shift (Python int is infinite precision,
            # but constraint guarantees n < 2^31 so this is safe)
            n >>= 1

        return count

        # ! sol2: Brian Kernighan's Algorithm ✅ (optimal / interview favourite)
        # Time:  O(k) where k = number of set bits  →  best case O(1), worst O(32)
        # Space: O(1)
        #
        # KEY INSIGHT: n & (n - 1) always clears the LOWEST set bit of n.
        #   Why? Subtracting 1 from n flips the lowest set bit to 0 and all
        #   lower bits to 1.  ANDing with original n cancels those lower bits.
        #
        #   Example:  n = 1100  (12)
        #             n-1 = 1011
        #             n & (n-1) = 1000  ← lowest set bit cleared!
        #
        #   So instead of iterating 32 times, we loop only as many times as
        #   there ARE set bits — ideal when the number is sparse in 1s.
        """
        Brian Kernighan's bit-clearing trick.

        Each iteration eliminates exactly one '1' bit:
            n = 10110100
            After 1st:  10110000  (cleared bit 2)
            After 2nd:  10100000  (cleared bit 4)
            After 3rd:  10000000  (cleared bit 5)
            After 4th:  00000000  (cleared bit 7)
            → 4 set bits, 4 iterations
        """
        count: int = 0
        while n:
            n &= n - 1  # drop the lowest set bit
            count += 1
        return count


# @lc code=end


#
# @lcpr case=start
# 11\n
# @lcpr case=end

# @lcpr case=start
# 128\n
# @lcpr case=end

# @lcpr case=start
# 2147483645\n
# @lcpr case=end

#
