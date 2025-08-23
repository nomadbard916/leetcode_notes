#
# @lc app=leetcode id=207 lang=python3
# @lcpr version=30201
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict, deque
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
        # some slot may not be used, but let's make all of them for convenience's sake
        # why not use dict? Using a list-of-lists works well here for a few reasons:
        # 1. Fixed Size:
        # The number of courses is known ahead of time (given by numCourses). This means the graph's size is fixed and we can initialize a list with numCourses empty lists directly. We don't need the flexibility of a dictionary.
        # 2. Performance:
        # Indexing into a list is O(1) and has lower overhead than dictionary lookups. This can be beneficial for performance in graph algorithms.
        # 3. Simplicity:
        # A list-of-lists clearly maps each course to its prerequisites (or adjacent courses) using 0-indexed integers. This is more straightforward than managing keys in a dictionary when the set of nodes is guaranteed to be consecutive integers.
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        def traverse(course: int):
            if self.has_cycle:
                return
            if self.on_path_nodes_list[course]:
                self.has_cycle = True
                return
            if self.visited[course]:
                return
            # preorder code
            self.visited[course] = True
            self.on_path_nodes_list[course] = True
            # traversal
            for unblocked_course in graph[course]:
                traverse(unblocked_course)
            # postorder code
            self.on_path_nodes_list[course] = False

        for course in range(numCourses):
            traverse(course)

        return not self.has_cycle

        # complexities
        # Time: O(V + E) for the same reasons
        # Space: O(V + E) for the graph and recursion stack (worst case O(V) depth)

        # !sol2: BFS + Topological Sort (Kahn's Algorithm)
        # Core Idea: Process courses with no prerequisites first, then gradually "unlock" other courses.
        # * build adjacency list graph and indegree array
        graph = defaultdict(list)
        # Track incoming edges (indegree) for each course
        # indegree[course] = number of prerequisites for this course
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # * initialize nodes in queue by indegree
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                # Find all courses with no prerequisites (indegree = 0)
                # These can be taken immediately
                q.append(course)

        completed_courses_cnt = 0
        # * BFS with template
        while q:
            # Take a course with no remaining prerequisites
            curr_course = q.popleft()
            completed_courses_cnt += 1
            for dependent_course in graph[curr_course]:
                # "Complete" it and reduce the prerequisite count for dependent courses
                indegree[dependent_course] -= 1
                # Add newly available courses to the queue. If it now has no prerequisites, it can be taken
                if indegree[dependent_course] == 0:
                    q.append(dependent_course)

        # if all the courses are processed, it means there's no circle
        return completed_courses_cnt == numCourses

        # complexities
        # Time: O(V + E) where V = numCourses, E = number of prerequisites
        # We visit each course once and each prerequisite edge once
        # Space: O(V + E) for the graph, indegree array, and queue

        # !sol3: DFS with three-color cycle detection
        # build adjacency list
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # color coding: 0=white, 1=gray, 2=black
        colors = [0] * numCourses

        def has_cycle(course: int) -> bool:
            """check if there's a cycle starting from this course"""
            # gray - black edge found, cycle detected
            if colors[course] == 1:
                return True
            # black - already processed, no cycle
            if colors[course] == 2:
                return False

            # mark currently processing as gray
            colors[course] = 1

            # check all dependent courses
            for dependent in graph[course]:
                if has_cycle(dependent):
                    return True

            # mark the completely processed as black
            colors[course] = 2
            return False

        # check each course for cycles
        for course_idx in range(numCourses):
            # only check unvisited courses
            if colors[course_idx] == 0:
                if has_cycle(course_idx):
                    return False

        return True


# @lc code=end


#
# @lcpr case=start
# 2\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[1,0],[0,1]]\n
# @lcpr case=end

#
