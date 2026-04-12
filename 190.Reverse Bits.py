#
# @lc app=leetcode id=190 lang=python3
# @lcpr version=30305
#
# [190] Reverse Bits
#

# @lc code=start


class Solution:
    def reverseBits(self, n: int) -> int:
        # ! sol1
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
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
