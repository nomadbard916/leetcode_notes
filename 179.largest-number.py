#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start


from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums: list = [str(num) for num in nums]

        def custom_sort(x: str, y: str):
            return int(x + y) - int(y + x)

        str_nums.sort(key=cmp_to_key(custom_sort), reverse=True)

        return "".join(str_nums) if str_nums[0] != "0" else "0"


# @lc code=end
