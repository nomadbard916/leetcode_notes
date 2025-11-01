#
# @lc app=leetcode id=417 lang=python3
# @lcpr version=30201
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque
from typing import List, Set, Tuple


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Key Insight: Reverse the Flow Direction
        # - Normal thinking (inefficient): For each cell, check if water can flow to both oceans.
        # This requires exploring from 417 cells potentially, with many redundant paths.

        # - Clever thinking (efficient): Start from the oceans and flow backward (upward in height).
        # We only do 2 complete searches instead of checking every cell.
        # Any cell visited by both searches can reach both oceans!

        # ! sol1: DFS
        """
        Find cells where water can flow to both Pacific and Atlantic oceans.

        Strategy: Instead of starting from each cell and checking if it reaches
        both oceans, we start from both oceans and find all reachable cells,
        that is going reversely to traverse to higher cell.

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

        # ! sol2: BFS, and is multi-source (every cell visited at most once)
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(queue: deque) -> Set[Tuple[int, int]]:
            # make all sources as visited upfront
            visited = set(queue)

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m
                        and 0 <= nc < n
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        # initialize queues with all border cells (multi source)
        pacific_q = deque()
        atlantic_q = deque()

        for c in range(n):
            pacific_q.append((0, c))
            atlantic_q.append((m - 1, c))
        for r in range(m):
            pacific_q.append((r, 0))
            atlantic_q.append((r, n - 1))

        pacific = bfs(pacific_q)
        atlantic = bfs(atlantic_q)

        return list(pacific & atlantic)

        # - Time Complexity: O(m × n)
        # Each cell is visited at most once by Pacific DFS and once by Atlantic DFS
        # Total: O(m × n) for Pacific + O(m × n) for Atlantic = O(m × n)

        # - Space Complexity: O(m × n)
        # Two sets storing reachable cells: O(m × n) each
        # DFS recursion stack: O(m × n) in worst case (entire grid is one path)
        # Total: O(m × n)

        # The BFS solution has similar complexity but may have better cache locality in practice.

        # DFS vs BFS Trade-offs
        # - DFS: Simpler code, uses recursion stack
        # - BFS: Iterative, better for finding shortest paths, more predictable memory usage


# @lc code=end


#
# @lcpr case=start
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#
