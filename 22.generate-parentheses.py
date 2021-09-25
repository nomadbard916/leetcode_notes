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

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + "(")
        if left < right:
            self.dfs(res, left, right - 1, path + ")")


# @lc code=end

