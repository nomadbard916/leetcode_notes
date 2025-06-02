#
# @lc app=leetcode id=207 lang=python3
# @lcpr version=30201
#
# [207] Course Schedule
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self):
        self.on_path_nodes_list: List[bool] = []
        self.visited: List[bool] = []
        self.has_cycle: bool = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ! sol1: DFS with cycle detection
        # record nodes in recursion stack
        # if visited nodes are checked redundantly, it will timeout => skip  "visited"
        self.on_path_nodes_list = [False] * numCourses
        self.visited = [False] * numCourses

        # * adjacency list is almost a must in a graph problem
        def build_graph(
            numCourses: int, prerequisites: List[List[int]]
        ) -> List[List[int]]:
            # some slot may not be used, but let's make all of them for convenience's sake
            # why not use dict? Using a list-of-lists works well here for a few reasons:
            # 1. Fixed Size:
            # The number of courses is known ahead of time (given by numCourses). This means the graph's size is fixed and we can initialize a list with numCourses empty lists directly. We don't need the flexibility of a dictionary.
            # 2. Performance:
            # Indexing into a list is O(1) and has lower overhead than dictionary lookups. This can be beneficial for performance in graph algorithms.
            # 3. Simplicity:
            # A list-of-lists clearly maps each course to its prerequisites (or adjacent courses) using 0-indexed integers. This is more straightforward than managing keys in a dictionary when the set of nodes is guaranteed to be consecutive integers.
            graph = [[] for _ in range(numCourses)]
            for edge in prerequisites:
                prior_course, latter_course = edge[1], edge[0]
                graph[prior_course].append(latter_course)
            return graph

        graph = build_graph(numCourses, prerequisites)

        def traverse(graph: List[List[int]], s: int):
            if self.has_cycle:
                return
            if self.on_path_nodes_list[s]:
                self.has_cycle = True
                return
            if self.visited[s]:
                return
            # preorder code
            self.visited[s] = True
            self.on_path_nodes_list[s] = True
            for t in graph[s]:
                traverse(graph, t)
            # postorder code
            self.on_path_nodes_list[s] = False

        for i in range(numCourses):
            traverse(graph, i)

        return not self.has_cycle


# @lc code=end


#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#
