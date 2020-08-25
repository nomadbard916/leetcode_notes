#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # as the calculation may be endless loop before reaching 1,
        # the ending condition needs to include if the current number is seen
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            current_sum = 0
            for d in str(n):
                current_sum += int(d) ** 2

            n = current_sum

        return n == 1


# @lc code=end

