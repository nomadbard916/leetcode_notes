#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure with path compression and union by rank.
    Used to efficiently group elements into disjoint sets and check connectivity.
    """

    def __init__(self, n: int):
        # Each element is initially its own parent
        self.parent = list(range(n))
        # Rank (approximate depth) of each tree
        self.rank = [0] * n
        # Number of distinct components
        self.count = 0

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # Path compression: make x point directly to root
            self.parent[x] = self.find(self.parent[x])
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        # Already in same set
        if root_x == root_y:
            return False

        # Union by rank: attach smaller tree under root of larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Same rank: make one root and increase its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        # Two components merged into one
        self.count -= 1

        return True

    def add_component(self) -> None:
        self.count += 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # !sol1: DFS
        # find the first island piece 1 and update counter,
        # modify it as 0 then iterate 4-direction of it, until there's no way to expend
        LENGTH, WIDTH = len(grid), len(grid[0])

        def dfs(grid, i, j):
            # mark it instead of using 'visited'
            grid[i][j] = "0"

            # iterating 4 directions with dFS
            upper_index = i - 1
            if upper_index >= 0 and grid[upper_index][j] == "1":
                dfs(grid, upper_index, j)

            lower_index = i + 1
            if lower_index < LENGTH and grid[lower_index][j] == "1":
                dfs(grid, lower_index, j)

            left_index = j - 1
            if left_index >= 0 and grid[i][left_index] == "1":
                dfs(grid, i, left_index)

            right_index = j + 1
            if right_index < WIDTH and grid[i][right_index] == "1":
                dfs(grid, i, right_index)

        counter = 0
        for i in range(LENGTH):
            for j in range(WIDTH):
                # only mark the first encounter of island piece, ignoring connected ones
                if grid[i][j] == "1":
                    counter += 1
                    dfs(grid, i, j)

        return counter

        # Time Complexity:
        # O(M × N)
        # Where M is the number of rows and N is the number of columns.
        # Each cell is visited at most once by the DFS.

        # Space Complexity:
        # O(M × N) in the worst case (if the entire grid is land, the recursion stack could go as deep as all cells).
        # There is no extra space used for a visited matrix, but the recursion stack can grow up to the total number of cells in the grid.

        # !sol2: union find
        # Union-Find is perfect for this problem because we're essentially finding connected components in a graph.
        # Each land cell is a node, and adjacent land cells are connected by edges.
        """
        Count the number of islands using Union-Find approach.

        Approach:
        1. Convert 2D grid positions to 1D indices for Union-Find
        2. For each land cell ('1'), check its right and down neighbors
        3. If neighbor is also land, union them (they're part of same island)
        4. Count total number of disjoint components containing land cells
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        def get_index(row: int, col: int) -> int:
            """Convert 2D coordinates to 1D index."""
            return row * cols + col

        # First pass: Add all land cells as individual components
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    uf.add_component()

        # Second pass: Union adjacent land cells
        # Only check right and down to avoid duplicate unions
        directions = [(0, 1), (1, 0)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    current_idx = get_index(row, col)

                    # Check right and down neighbors
                    for dr, dc in directions:
                        new_row, new_col = row + dr, col + dc

                        # If neighbor is valid and is land
                        if (
                            0 <= new_row < rows
                            and 0 <= new_col < cols
                            and grid[new_row][new_col] == "1"
                        ):
                            neighbor_idx = get_index(new_row, new_col)
                            uf.union(current_idx, neighbor_idx)
        return uf.count

        # time complexity:
        # O(M × N × α(M × N))
        # α is the inverse Ackermann function (practically constant ≤ 4)
        # So effectively O(M × N) as well

        # space complexity
        # O(M × N) for parent and rank arrays

        # When to Use Each Approach:
        # Use DFS when:
        # - Simple one-time component counting
        # - You can modify the input grid
        # - Recursion depth isn't a concern

        # Use Union-Find when:
        # - Need to handle dynamic connectivity (adding/removing edges)
        # - Multiple queries about connectivity
        # - Want iterative solution (no recursion)
        # - Building foundation for more complex graph problems


# @lc code=end
