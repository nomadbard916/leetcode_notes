"""
UNION FIND (DISJOINT SET UNION) - COMPLETE TUTORIAL
==================================================

Union Find is a data structure that efficiently handles dynamic connectivity queries.
Think of it as answering: "Are these two elements connected?" and "Connect these two elements!"

REAL WORLD ANALOGY:
Imagine you're organizing people into friendship groups at a party. You want to:
1. Quickly check if two people are in the same friend group
2. Merge two friend groups when you discover a connection between them

This is exactly what Union Find does!
"""


class BasicUnionFind:
    """
    The most basic implementation - helps us understand the core concepts
    """

    def __init__(self, n):
        # Each element starts as its own parent (separate group)
        # Think: Everyone starts as their own friend group
        self.parent = list(range(n))
        self.size = n

    def find(self, x):
        """
        Find the root/representative of the set containing x

        Why we need this: To check if two elements are connected,
        we see if they have the same root
        """
        if self.parent[x] != x:
            # If x is not its own parent, keep going up the chain
            return self.find(self.parent[x])
        return x

    def union(self, x, y):
        """
        Connect two elements by merging their sets

        The key insight: Make one root point to the other
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # They're in different sets, so merge them
            self.parent[root_x] = root_y

    def connected(self, x, y):
        """Check if two elements are in the same connected component"""
        return self.find(x) == self.find(y)


class OptimizedUnionFind:
    """
    Production-ready version with crucial optimizations
    """

    def __init__(self, n):
        self.parent = list(range(n))  # Each node points to itself initially
        self.rank = [0] * n  # Height of each tree (for union by rank)
        self.size = [1] * n  # Size of each component (alternative to rank)
        self.num_components = n  # Total number of separate components

    def find(self, x):
        """
        Find with PATH COMPRESSION - the key optimization!

        Path compression makes the tree flat by pointing every node
        directly to the root. This makes future operations nearly O(1).

        Think of it like: Once you find who the "ultimate boss" is,
        you remember it for next time instead of going through the chain again.
        """
        if self.parent[x] != x:
            # This is the magic line - path compression!
            # We recursively find the root AND update parent[x] to point directly to it
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_by_rank(self, x, y):
        """
        Union by rank optimization: Always attach smaller tree to larger tree

        Why? This keeps the tree height minimal, making find operations faster
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already connected

        # Union by rank: attach smaller tree to larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Same rank: choose arbitrarily, but increment rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.num_components -= 1
        return True  # Successfully merged

    def union_by_size(self, x, y):
        """
        Alternative to union by rank: merge based on component size

        Some prefer this because size has a clear meaning, while rank is more abstract
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Always attach smaller component to larger one
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x  # Swap to ensure root_x is larger

        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.num_components -= 1
        return True

    def connected(self, x, y):
        """Check if two elements belong to the same component"""
        return self.find(x) == self.find(y)

    def get_component_size(self, x):
        """Get the size of the component containing x"""
        return self.size[self.find(x)]

    def get_num_components(self):
        """Get total number of separate components"""
        return self.num_components


def demonstrate_union_find():
    """
    Let's walk through a concrete example to see Union Find in action!

    Scenario: We have 6 people (0,1,2,3,4,5) and we're tracking friendships
    """
    print("=== UNION FIND DEMONSTRATION ===\n")

    uf = OptimizedUnionFind(6)
    print(f"Initial state: {uf.num_components} separate people")
    print(f"Parent array: {uf.parent}")
    print()

    # Person 0 becomes friends with Person 1
    print("Step 1: Connect 0 and 1 (they become friends)")
    uf.union_by_size(0, 1)
    print(f"Components: {uf.num_components}")
    print(f"Parent array: {uf.parent}")
    print(f"Are 0 and 1 connected? {uf.connected(0, 1)}")
    print()

    # Person 2 becomes friends with Person 3
    print("Step 2: Connect 2 and 3")
    uf.union_by_size(2, 3)
    print(f"Components: {uf.num_components}")
    print(f"Parent array: {uf.parent}")
    print()

    # Person 1 becomes friends with Person 2 (this merges two friend groups!)
    print("Step 3: Connect 1 and 2 (this merges the {0,1} and {2,3} groups!)")
    uf.union_by_size(1, 2)
    print(f"Components: {uf.num_components}")
    print(f"Parent array: {uf.parent}")
    print(f"Are 0 and 3 connected? {uf.connected(0, 3)} (through 1-2 connection)")
    print(f"Size of component containing 0: {uf.get_component_size(0)}")
    print()

    # Check various connections
    print("Final connection checks:")
    print(f"0 and 3 connected: {uf.connected(0, 3)}")
    print(f"0 and 4 connected: {uf.connected(0, 4)}")
    print(f"4 and 5 connected: {uf.connected(4, 5)}")


def solve_number_of_islands():
    """
    Classic problem: Count islands in a 2D grid

    This shows how Union Find can solve graph problems elegantly
    """
    print("\n=== SOLVING: NUMBER OF ISLANDS ===\n")

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    def num_islands_union_find(grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        # Convert 2D coordinates to 1D index for Union Find
        def get_index(r, c):
            return r * cols + c

        # Count water cells to subtract from total later
        water_cells = 0
        uf = OptimizedUnionFind(rows * cols)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    water_cells += 1
                else:
                    # For each land cell, connect it to adjacent land cells
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            uf.union_by_size(get_index(r, c), get_index(nr, nc))

        # Islands = total components - water cells
        return uf.get_num_components() - water_cells

    result = num_islands_union_find(grid)
    print(f"Grid:")
    for row in grid:
        print(row)
    print(f"\nNumber of islands: {result}")


def solve_redundant_connection():
    """
    Another classic: Find the edge that makes a tree into a graph with a cycle

    This showcases Union Find's cycle detection capability
    """
    print("\n=== SOLVING: REDUNDANT CONNECTION ===\n")

    def find_redundant_connection(edges):
        """
        Key insight: In a tree with n nodes, we need exactly n-1 edges.
        If we have n edges, exactly one is redundant.

        We process edges one by one. The first edge that connects
        two already-connected nodes is the redundant one!
        """
        n = len(edges)
        uf = OptimizedUnionFind(n + 1)  # nodes are 1-indexed

        for u, v in edges:
            if uf.connected(u, v):
                # These nodes are already connected through some path
                # This edge creates a cycle!
                return [u, v]
            uf.union_by_size(u, v)

        return []  # Should never reach here for valid input

    edges = [[1, 2], [1, 3], [2, 3]]
    result = find_redundant_connection(edges)
    print(f"Edges: {edges}")
    print(f"Redundant connection: {result}")
    print(
        "Explanation: Edges [1,2] and [1,3] already connect nodes 2 and 3 through node 1"
    )


def time_complexity_analysis():
    """
    Understanding the time complexity is crucial for interviews!
    """
    print("\n=== TIME COMPLEXITY ANALYSIS ===\n")

    print("Without optimizations:")
    print("- Find: O(n) worst case (imagine a long chain)")
    print("- Union: O(n) worst case (needs to call find)")
    print()

    print("With Path Compression only:")
    print("- Amortized O(log n) per operation")
    print()

    print("With Union by Rank/Size only:")
    print("- O(log n) per operation")
    print()

    print("With BOTH optimizations (Path Compression + Union by Rank):")
    print("- O(α(n)) amortized per operation")
    print("- α(n) is the inverse Ackermann function")
    print("- For all practical purposes, α(n) ≤ 4")
    print("- This is essentially O(1) for real-world inputs!")
    print()

    print("Why is this so fast?")
    print("- Path compression flattens trees over time")
    print("- Union by rank keeps trees shallow")
    print("- Together, they create nearly flat structures")


if __name__ == "__main__":
    demonstrate_union_find()
    solve_number_of_islands()
    solve_redundant_connection()
    time_complexity_analysis()

    print("\n=== KEY TAKEAWAYS ===")
    print("1. Union Find excels at dynamic connectivity problems")
    print("2. Path compression + union by rank gives near O(1) operations")
    print("3. Perfect for: cycle detection, connected components, MST algorithms")
    print("4. Common pattern: process elements one by one, union as you go")
    print("5. Remember: find() gives you the representative of a component")
