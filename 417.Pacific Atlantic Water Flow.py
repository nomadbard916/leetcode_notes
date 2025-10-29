#
# @lc app=leetcode id=417 lang=python3
# @lcpr version=30201
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # ! sol1: DFS
        """
        Find cells where water can flow to both Pacific and Atlantic oceans.

        Strategy: Instead of starting from each cell and checking if it reaches
        both oceans, we start from both oceans and find all reachable cells.
        The intersection gives us cells that can reach both oceans.
        """
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        # sets to track cells reachable from each ocean
        pacific_reachable: Set[Tuple[int, int]] = set()
        atlantic_reachable: Set[Tuple[int, int]] = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(
            row: int, col: int, reachable: Set[Tuple[int, int]], prev_height: int
        ) -> None:
            """
            DFS to find all cells reachable from an ocean.

            Args:
                row, col: Current cell position
                reachable: Set to store reachable cells
                prev_height: Height of previous cell (water flows upward in reverse)
            """
            # boundary check
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            # already visited or water can't flow here (current height < previous)
            if (row, col) in reachable or heights[row][col] < prev_height:
                return

            # mark as reachable
            reachable.add((row, col))

            # explore all 4 directions
            for dr, dc in directions:
                dfs(row + dr, col + dc, reachable, heights[row][col])

        # start DFS from all Pacific border cells (top row and left column)
        for col in range(n):
            dfs(0, col, pacific_reachable, heights[0][col])  # top row
        for row in range(m):
            dfs(row, 0, pacific_reachable, heights[row][0])  # left column

        # start DFS from all Atlantic border cells (bottom row and right column)
        for col in range(n):
            dfs(m - 1, col, atlantic_reachable, heights[m - 1][col])  # bottom row
        for row in range(m):
            dfs(row, n - 1, atlantic_reachable, heights[row][n - 1])  # right column

        # find intersection: cells reachable from both oceans
        return list(pacific_reachable & atlantic_reachable)


# @lc code=end


#
# @lcpr case=start
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#
