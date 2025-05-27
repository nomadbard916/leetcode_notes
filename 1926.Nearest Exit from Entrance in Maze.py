#
# @lc app=leetcode id=1926 lang=python3
# @lcpr version=30104
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # setting up consts
        m = len(maze)
        n = len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # * BFS framework with visited
        q = deque()
        q.append(entrance)
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[entrance[0]][entrance[1]] = True

        steps = 1
        while q:
            # records children nodes counts of current level
            q_size = len(q)
            # visit all the nodes of the same level
            for _ in range(q_size):
                cur_node = q.popleft()
                # try to step out 1 step in dirs
                for dir in dirs:
                    x = cur_node[0] + dir[0]
                    y = cur_node[1] + dir[1]
                    # out of bound
                    if (
                        x < 0
                        or x >= m
                        or y < 0
                        or y >= n
                        or visited[x][y]
                        or maze[x][y] == "+"
                    ):
                        continue
                    # if it's exit
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        return steps
                    # record node
                    visited[x][y] = True
                    q.append([x, y])
            steps += 1
        return -1


# @lc code=end


#
# @lcpr case=start
# [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]\n[1,2]\n
# @lcpr case=end

# @lcpr case=start
# [["+","+","+"],[".",".","."],["+","+","+"]]\n[1,0]\n
# @lcpr case=end

# @lcpr case=start
# [[".","+"]]\n[0,0]\n
# @lcpr case=end

#
