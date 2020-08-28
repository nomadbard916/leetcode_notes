#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # eg. 6! == 6 * (5) * 4 * 3 * (2) *1
        # therefore finding the count of 5 in factorial derives the count of 10
        # originally it needs to find 10, now it only need to find half of it ie. 5, so the time complexity cuts to O(log(n))

        count = 0
        while n > 0:
            n //= 5
            count += n

        return count


# @lc code=end

