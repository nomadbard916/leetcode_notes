#
# @lc app=leetcode id=210 lang=python3
# @lcpr version=30104
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict, deque
from typing import List


class Solution:
    def __init__(self):
        self.postorder_res = []
        self.has_cycle = False
        self.visited = []
        self.on_path = []

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # ! sol1: DFS with topological sort
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        self.visited = [False] * numCourses
        self.on_path = [False] * numCourses

        def traverse(graph: List[List[int]], s: int):
            if self.on_path[s]:
                self.has_cycle = True
            if self.visited[s] or self.has_cycle:
                return
            # preorder processing
            self.on_path[s] = True
            self.visited[s] = True
            for t in graph[s]:
                traverse(graph, t)
            # postorder code
            self.postorder_res.append(s)
            self.on_path[s] = False

        for i in range(numCourses):
            traverse(graph, i)
        # non-DAG cannot do topological sort
        if self.has_cycle:
            return []
        # * the result of topological sort is the result of post-order traversal
        self.postorder_res.reverse()
        return self.postorder_res

        # ! sol2: BFS with Kahn's Algorithm
        # * step 1: build adjacency list and calculate in-degrees
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # * step 2: find all courses with no prerequisites (in-degree = 0)
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        # * step 3: process courses in topological order
        result = []

        while q:
            # Take a course with no remaining prerequisites
            curr_course = q.popleft()
            result.append(curr_course)

            for dependent_course in graph[curr_course]:
                in_degree[dependent_course] -= 1

                if in_degree[dependent_course] == 0:
                    q.append(dependent_course)

        # * Step 4: Check if we processed all courses
        # If we couldn't process all courses, there's a cycle
        if len(result) != numCourses:
            return []
        return result


# @lc code=end


#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[[1,0],[2,0],[3,1],[3,2]]\n
# @lcpr case=end

# @lcpr case=start
# 1\n[]\n
# @lcpr case=end

#
