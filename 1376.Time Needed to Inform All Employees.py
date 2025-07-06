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
        subordinates = {}
        for i in range(n):
            subordinates[i] = []

        for employee_id in range(n):
            if manager[employee_id] != -1:
                subordinates[manager[employee_id]].append(employee_id)

        def dfs(employee_id: int) -> int:
            if not subordinates[employee_id]:
                return 0
            max_subordina_time = 0
            for subordinate in subordinates[employee_id]:
                subordinate_total_time = dfs(subordinate)
                max_subordina_time = max(max_subordina_time, subordinate_total_time)

            return informTime[employee_id] + max_subordina_time

        return dfs(headID)


# @lc code=end


#
# @lcpr case=start
# 1\n0\n[-1]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# 6\n2\n[2,2,-1,2,2,2]\n[0,0,1,0,0,0]\n
# @lcpr case=end

#
