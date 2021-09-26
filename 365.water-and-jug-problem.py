#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start
class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        if targetCapacity == 0:
            return True

        # ax+by=z, where possible solution d = c * gcd(x,y)
        return (
            jug1Capacity + jug2Capacity >= targetCapacity
            and targetCapacity % self.gcd(jug1Capacity, jug2Capacity) == 0
        )

    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)


# @lc code=end

