#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # sol1: stack, monotonic
        # Monotonic stacks are a good option when a problem involves comparing
        # the size of numeric elements, with their order being relevant.
        stack = []  # data format: (t, i), with t keep decreasing after popped
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # concept of "monotonic stack" here
            while stack and stack[-1][0] < t:
                # top_t is stack.pop()[0],
                # which was checked against in 'while' condition and not used here
                top_i = stack.pop()[1]
                ans[top_i] = i - top_i

            stack.append((t, i))

        return ans

        # sol2: hash map


# @lc code=end
