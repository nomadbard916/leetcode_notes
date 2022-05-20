#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrack with DFS
        ans = []
        self.backtrack(ans, n, n, "")
        return ans

    def backtrack(
        self, ans: list, left_addable: int, right_addable: int, current_path: str
    ):
        # right can be added when there's more left than right
        if left_addable == 0 and right_addable == 0:
            ans.append(current_path)
            return

        if left_addable > 0:
            self.backtrack(ans, left_addable - 1, right_addable, current_path + "(")
        # add ) when there's more ( than )
        if left_addable < right_addable:
            self.backtrack(ans, left_addable, right_addable - 1, current_path + ")")


# @lc code=end
