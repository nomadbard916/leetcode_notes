#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrack with DFS or BFS
        res = []
        self.dfs(res, n, n, "")
        return res

    def dfs(self, res, left_addable, right_addable, path):
        # right can be added when there's more left than right
        if left_addable == 0 and right_addable == 0:
            res.append(path)
            return
        if left_addable > 0:
            self.dfs(res, left_addable - 1, right_addable, path + "(")
        # add ) when there's more ( than )
        if left_addable < right_addable:
            self.dfs(res, left_addable, right_addable - 1, path + ")")


# @lc code=end

