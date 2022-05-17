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

        # assume every 1 is unreachable before actually calculating
        distances = [[INF_INT] * n for _ in range(m)]
        q = collections.deque()

        # start from 0 to update 1, or time complexity will be high
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    # initialize distance as every 0 has zero distance to 0, i.e. itself
                    distances[i][j] = 0
                    q.append((j, i))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            cur_x, cur_y = q.popleft()
            # iterate four directions
            for dx, dy in directions:
                new_x, new_y = cur_x + dx, cur_y + dy

                new_x_y_could_update = (
                    0 <= new_x < n and 0 <= new_y < m and mat[new_y][new_x] == 1
                )
                if not new_x_y_could_update:
                    continue

                cur_distance = distances[cur_y][cur_x]
                # means it's cell '1' still at initial state,
                # and should be visited exactly once
                if distances[new_y][new_x] == INF_INT:
                    distances[new_y][new_x] = cur_distance + 1
                    q.append((new_x, new_y))

        return distances

        # sol 2: in-place update
        # q = collections.deque()
        # row = len(matrix)
        # col = len(matrix[0])
        # dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        # for x in range(row):
        #     for y in range(col):
        #         if matrix[x][y] == 0:
        #             q.append((x, y))
        #         else:
        #             matrix[x][y] = float("inf")
        # while q:
        #     x, y = q.popleft()
        #     for dx, dy in dirs:
        #         new_x, new_y = x + dx, y + dy
        #         if (
        #             0 <= new_x < row
        #             and 0 <= new_y < col
        #             and matrix[new_x][new_y] > matrix[x][y] + 1
        #         ):
        #             q.append((new_x, new_y))
        #             matrix[new_x][new_y] = matrix[x][y] + 1
        # return matrix

        # sol3: start from 1 to update 0. remember to mark 'visited'
        # def bfs(i, j):
        #     q = collections.deque()
        #     q.append((i, j))
        #     visited = set()
        #     visited.add((i, j))
        #     step = -1
        #     flag = False
        #     while q:
        #         if flag:
        #             break
        #         _len = len(q)
        #         step += 1
        #         for _ in range(_len):
        #             curr = q.popleft()
        #             if matrix[curr[0]][curr[1]] == 0:
        #                 flag = True
        #                 break

        #             dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        #             for d in dirs:
        #                 x = curr[0] + d[0]
        #                 y = curr[1] + d[1]
        #                 if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
        #                     visited.add((x, y))
        #                     q.append((x, y))

        #     return step

        # m = len(matrix)
        # n = len(matrix[0])
        # ans = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 1:
        #             ans[i][j] = bfs(i, j)
        # return ans


# @lc code=end
