class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路徑壓縮
        return self.parent[x]

    def union(self, x, q):
        rootX = self.find(x)
        rootY = self.find(q)

        if rootX != rootY:
            # 按size (rank)合併
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def test():
    # Example

    # ID = 0, 1, 2, ..., 9
    ds = DisjointSet(10)

    print("After initialization")
    for i in range(10):
        print(f"root of {i} = {ds.find(i)}")

    ds.union(1, 2)

    print("\nAfter union(1, 2)")
    for i in range(10):
        print(f"root of {i} = {ds.find(i)}")

    ds.union(3, 4)

    print("\nAfter union(1, 2) and union(3, 4)")
    for i in range(10):
        print(f"root of {i} = {ds.find(i)}")

    ds.union(1, 3)
    print("\nAfter union(1, 2), union(3, 4), union(1, 3)")
    for i in range(10):
        print(f"root of {i} = {ds.find(i)}")


if __name__ == "__main__":
    test()
#  https://vocus.cc/article/66d07767fd8978000147a3ad
