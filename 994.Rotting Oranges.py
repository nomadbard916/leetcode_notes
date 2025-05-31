#
# @lc app=leetcode id=994 lang=python3
# @lcpr version=30201
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh_count = 0

        # Step 1: Find all initially rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        # step 2: BFS o rot adjacent fresh oranges
        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q and fresh_count > 0:
            minutes += 1
            # Process all oranges that are rotten at the current minute
            q_size = len(q)
            for _ in range(q_size):
                row, col = q.popleft()

                # check all directions
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    # get the fresh orange
                    # trick: new_row and new_col may be out of range,
                    # so checking if it is fresh orange should be the lastly chained for if condition
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        q.append((new_row, new_col))

        if fresh_count == 0:
            return minutes

        return -1


# @lc code=end


#
# @lcpr case=start
# [[2,1,1],[1,1,0],[0,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,1],[0,1,1],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,2]]\n
# @lcpr case=end

#
