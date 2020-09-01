#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        value_length = 1
        digit_count = 9
        starting_value = 1

        while n > value_length * digit_count:
            n -= value_length * digit_count
            value_length += 1
            digit_count *= 10
            starting_value *= 10

        starting_value += (n - 1) // value_length

        return int(str(starting_value)[(n - 1) % value_length])


# @lc code=end

