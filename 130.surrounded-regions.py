#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
import collections
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # thinking negatively: all the border O and neighbors are not surroundable
        # => all the other O are surrounded regions
        # BFS

        if not board:
            return

        m, n = len(board), len(board[0])
        q = collections.deque()

        # get all the positions of O on border
        for r in range(m):
            for c in range(n):
                if (r in [0, m - 1] or c in [0, n - 1]) and board[r][c] == "O":
                    q.append((r, c))

        # bfs, protect these border O and neighbors by converting first to 'D'
        while q:
            x, y = q.popleft()
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                board[x][y] = "D"
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    q.append((x + dx, y + dy))

        # convert the rest of O to X and protected D to O
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "D":
                    board[r][c] = "O"


# @lc code=end

