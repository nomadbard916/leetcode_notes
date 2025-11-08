#
# @lc app=leetcode id=329 lang=python3
# @lcpr version=30201
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # !sol1: DFS with memo
        # * it's totally fine to go plain DFS at first, but you'll immediately encounter TLE
        # * Why DFS?
        # - We need to explore all possible paths from each cell
        # - DFS naturally follows a path to its end before backtracking

        # * Why Memoization?
        # - Without caching, we'd recalculate the same cell's longest path many times, which is essentially "overlapping subproblems"
        # - Example: If cells A, B, and C all connect to cell D, we'd calculate D's longest path 3 times
        # - Memoization stores results so each cell is computed only once
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        # memo: cache[i][]j stores the longest path starting from (i,j)
        cache: List[List[int]] = [[0] * cols for _ in range(rows)]

        def dfs(row: int, col: int) -> int:
            # if already computed, return cached result
            if cache[row][col] != 0:
                return cache[row][col]

            # base case: min path length is  (the cell itself)
            max_length = 1

            # Explore all 4 directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check if the new position is valid and has a greater value
                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and matrix[new_row][new_col] > matrix[row][col]
                ):
                    # Recursively find the longest path from the neighbor
                    # Add 1 to include the current cell
                    length = 1 + dfs(new_row, new_col)
                    max_length = max(max_length, length)

            # Cache the result before returning
            cache[row][col] = max_length
            return max_length

        # try starting from every cell and find the maximum
        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))

        return result

        # Complexity Analysis
        # Time Complexity: O(m × n)
        # - We have m×n cells
        # - Each cell is computed exactly once due to memoization
        # - For each cell, we check 4 directions: O(1)
        # - Total: O(m × n)

        # Space Complexity: O(m × n)
        # - Cache array: O(m × n)
        # - Recursion stack: O(m × n) in worst case (imagine a path that goes through all cells)
        # - Total: O(m × n)

        # ! sol2: BFS with topological sort
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])

        # count how many neighbors have smaller values (in-degree)
        in_degree: List[List[int]] = [[0] * cols for _ in range(rows)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # calculate in-degree
        for i in range(rows):
            for j in range(cols):
                for dr, dc in directions:
                    ni, nj = i + dr, j + dc
                    if (
                        0 <= ni < rows
                        and 0 <= nj < cols
                        and matrix[ni][nj] < matrix[i][j]
                    ):
                        in_degree[i][j] += 1

        # Start with cells that have no smaller neighbors (in-degree = 0)
        queue: deque = deque
        for i in range(rows):
            for j in range(cols):
                if in_degree[i][j] == 0:
                    queue.append((i, j))

        # process level by level (BFS)
        max_length = 0
        while queue:
            max_length += 1
            # process all cells at current level
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # Check all neighbors with larger values
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and matrix[new_row][new_col] > matrix[row][col]
                    ):
                        in_degree[new_row][new_col] -= 1
                        # If all smaller neighbors processed, add to queue
                        if in_degree[new_row][new_col] == 0:
                            queue.append((new_row, new_col))

        return max_length

        # Complexity Analysis (Sol2 - BFS / Topological Sort)
        # Time Complexity: O(m * n)
        # - Computing the in-degree for every cell visits each cell and checks up to 4 neighbors: O(mn)
        # - During the BFS, each cell is pushed/popped at most once and for each cell we inspect up to 4 neighbors: O(mn)
        # - Total: O(mn)

        # Space Complexity: O(m * n)
        # - The in_degree matrix stores one integer per cell: O(mn)
        # - The BFS queue can hold up to O(mn) cells in the worst case (e.g., all cells on the same level)
        # - Additional constant-space arrays (directions) are O(1)
        # - Total: O(mn)


# @lc code=end


#
# @lcpr case=start
# [[9,9,4],[6,6,8],[2,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,4,5],[3,2,6],[2,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

#
