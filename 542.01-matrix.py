#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
import collections
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS
        m, n = len(mat), len(mat[0])
        # fake a very big integer as inf
        INF_INT = 2**99
        distances = [[INF_INT] * n for _ in range(m)]
        q = collections.deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    # initialize distance and append
                    distances[i][j] = 0
                    q.append((j, i))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            cur_x, cur_y = q.popleft()
            # iterate four directions
            for dx, dy in directions:
                new_x, new_y = cur_x + dx, cur_y + dy

                new_x_y_should_update = (
                    0 <= new_x < n and 0 <= new_y < m and mat[new_y][new_x] == 1
                )
                if not new_x_y_should_update:
                    continue

                cur_distance = distances[cur_y][cur_x]
                if distances[new_y][new_x] == INF_INT:
                    distances[new_y][new_x] = cur_distance + 1
                    q.append((new_x, new_y))

        return distances


# @lc code=end
