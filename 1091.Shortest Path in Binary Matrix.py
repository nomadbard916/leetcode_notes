#
# @lc app=leetcode id=1091 lang=python3
# @lcpr version=30104
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
import collections
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # sanity checks:
        # start or end cell is blocked
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # single cell matrix
        if n == 1:
            return 1

        #  8 directions: up, down, left, right, and 4 diagonals
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        # * BFS setup
        # You cannot use a single variable to track path length because BFS explores multiple paths simultaneously.
        # The Core Issue: BFS processes nodes in "waves" or "levels".
        # At any given moment, your queue contains nodes from potentially different distances from the start.
        # A single path_length variable can't track multiple different distances simultaneously.

        # Key Learning: In BFS, you're not following a single path -
        # you're exploring ALL possible paths simultaneously, layer by layer.
        # Each node in the queue represents a different potential path, so each needs its own distance tracking.

        # The global variable "path depth" is more suitable for binary tree traversal problems
        # Why Global Depth Works in Trees:
        # - Single path to each node: In a tree, there's exactly one path from root to any node
        # - Level-synchronized: All nodes at the same level have the same depth
        # - No cycles: Can't revisit nodes, so no path length confusion
        q = collections.deque([(0, 0, 1)])  # (row, col, path_length)
        visited = set()
        visited.add((0, 0))

        while q:
            row, col, path_length = q.popleft()

            # check if we reached the destination
            dest_idx = n - 1
            if row == dest_idx and col == dest_idx:
                return path_length

            # explore all 8 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # only traverse to  new position when it's valid
                still_inbound = 0 <= new_row < n and 0 <= new_col < n
                valid_cell_val = grid[new_row][new_col] == 0
                new_cell_not_visited = (new_row, new_col) not in visited
                if still_inbound and valid_cell_val and new_cell_not_visited:
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col, path_length + 1))

        # finally not found
        return -1

        # Time Complexity: O(n²)
        # In worst case, we visit all cells in the n×n grid once
        # Each cell operation (checking neighbors, queue operations) is O(1)

        # Space Complexity: O(n²)
        # Visited set can contain up to n² cells
        # Queue can contain up to n² cells in worst case

        # sol2: using "steps" variable
        """
        ALTERNATIVE VERSION: Using steps variable with level-by-level BFS
        """
        n = len(grid)

        # Edge case: start or end cell is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # Edge case: single cell matrix
        if n == 1:
            return 1

        # 8 directions: up, down, left, right, and 4 diagonals
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        # BFS setup - only store coordinates
        queue = deque([(0, 0)])  # (row, col)
        visited = set()
        visited.add((0, 0))
        steps = 1  # Global step counter

        while queue:
            # KEY: Process all nodes at current level before moving to next level
            level_size = len(queue)

            for _ in range(level_size):
                row, col = queue.popleft()

                # Check if we reached the destination
                if row == n-1 and col == n-1:
                    return steps

                # Explore all 8 directions
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # Check if new position is valid
                    if (0 <= new_row < n and 0 <= new_col < n and
                        grid[new_row][new_col] == 0 and
                        (new_row, new_col) not in visited):

                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

            # Increment steps after processing entire current level
            steps += 1

        return -1  # No path found


# @lc code=end


#
# @lcpr case=start
# [[0,1],[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[1,1,0],[1,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#
