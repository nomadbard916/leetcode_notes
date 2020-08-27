#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        converted = "".join(list(map(lambda x: str(x), digits)))
        calculated = str(int(converted) + 1)

        return list(map(lambda x: int(x), list(calculated)))


# @lc code=end

