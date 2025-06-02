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
        self.on_path_nodes_list = []
        self.visited = []
        self.has_cycle = False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # ! sol1: DFS with cycle detection
        # record nodes in recursion stack
        # if visited nodes are checked redundantly, it will timeout => skip  "visited"
        self.on_path_nodes_list = [False] * numCourses
        self.visited = [False] * numCourses

        def build_graph(
            numCourses: int, prerequisites: List[List[int]]
        ) -> List[List[int]]:
            graph = [[] for _ in range(numCourses)]
            for edge in prerequisites:
                from_node, to_node = edge[1], edge[0]
                graph[from_node].append(to_node)
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
