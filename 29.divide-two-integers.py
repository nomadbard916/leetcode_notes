#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # any number can be: a* 2**n + b * 2**(n-1)...... + y*2**1 +z* 2**0
        # https://blog.csdn.net/lym940928/article/details/90770201

        MIN_INT = -(2 ** 31)
        MAX_INT = 2 ** 31 - 1

        sign = 1 if (dividend > 0) == (divisor > 0) else -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            # need to start from power 1 every time as it cannot be certain exactly how many timed divisor need to be multiplied
            current_power = 1
            current_divisor = divisor

            # acceleration
            while dividend >= current_divisor:
                dividend -= current_divisor  # get remaining part of dividend
                result += current_power

                current_power <<= 1
                current_divisor <<= 1

        result *= sign

        return max(min(result, MAX_INT), MIN_INT)


# @lc code=end

