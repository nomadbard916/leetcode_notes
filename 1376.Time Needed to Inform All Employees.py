#
# @lc app=leetcode id=1376 lang=python3
# @lcpr version=30201
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
from typing import List


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        # ! sol1: DFS
        # * Build adjacency list representation of the company hierarchy
        # {manager_id: [...subordinates]}
        subordinates = {}
        for manager_id in range(n):
            subordinates[manager_id] = []

        for employee_id in range(n):
            manager_id = manager[employee_id]
            # -1 indicates this is the head (no manager)
            if manager_id != -1:
                subordinates[manager_id].append(employee_id)

        def dfs(employee_id: int) -> int:
            # Base case: if this employee has no subordinates (leaf node), no  time needed
            if not subordinates[employee_id]:
                return 0

            # Find the maximum time among all subordinates
            max_subordinate_time = 0
            for subordinate_id in subordinates[employee_id]:
                subordinate_total_time = dfs(subordinate_id)
                max_subordinate_time = max(max_subordinate_time, subordinate_total_time)

            # * post order logic
            # Total time = time for this employee to inform + max time for subordinates
            return informTime[employee_id] + max_subordinate_time

        # Start DFS from the head of company
        return dfs(headID)

        # Time and Space Complexity:
        # Time Complexity: O(n) - We visit each employee exactly once
        # Space Complexity: O(n) - For the adjacency list and recursion stack (in worst case of skewed tree)

        # ! sol2: BFS, but it doesn't have strong advantage


# @lc code=end


#
# @lcpr case=start
# 1\n0\n[-1]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# 6\n2\n[2,2,-1,2,2,2]\n[0,0,1,0,0,0]\n
# @lcpr case=end

#
