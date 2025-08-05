#
# @lc app=leetcode id=1235 lang=python3
# @lcpr version=30201
#
# [1235] Maximum Profit in Job Scheduling
#

# @lc code=start
from bisect import bisect_right
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        # Why This Problem is Perfect for DP, not backtracking:
        # - Overlapping Subproblems: The same "maximum profit from jobs starting at index i"
        # gets computed multiple times in pure backtracking
        # - Optimal Substructure: The optimal solution contains optimal solutions to subproblems
        # - Clear State: We can uniquely identify each subproblem by the current job index

        # ! sol1: pure DP
        n = len(startTime)

        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])  # Sort by end time

        # If you choose a job that ends at time X, you will be able to start another job that starts at time X.
        # => just focus on end time
        # This is crucial because it allows us to make optimal decisions in order -
        # when we reach job i, we've already computed the optimal solution for all jobs that end before job i.
        end_times = [job[1] for job in jobs]

        # dp[i] represents maximum profit using jobs 0 to i.
        # The information is accumulative; every position includes the info from previous positions.
        # Every dp[i] contains the OPTIMAL solution that already considers ALL previous positions (0 to i).
        dp_max_profit = [0] * n
        dp_max_profit[0] = jobs[0][2]

        # careful: positions start from 1, not index 0
        for i in range(1, n):
            curr_start, curr_end, curr_profit = jobs[i]

            # * state for i dp[i]: greater of taking the job vs. not taking
            # Option 1: Don't take current job, so the profix is only about previous max
            profit_without_curr = dp_max_profit[i - 1]

            # Option 2: Take current job
            # "What's the best profit I could have made from all the jobs that happened BEFORE this one?"
            # Find the latest job that doesn't overlap with current job
            # We need a job that ends before curr_start
            # bisect_right() finds the first position where end_time > current_start.
            # Subtracting 1 gives us the last position where end_time ≤ current_start.
            latest_non_overlap_idx = bisect_right(end_times, curr_start) - 1

            # exists
            if latest_non_overlap_idx >= 0:
                profit_with_curr = dp_max_profit[latest_non_overlap_idx] + curr_profit
            # doesn't exist
            else:
                profit_with_curr = curr_profit

            # Take maximum of both options
            dp_max_profit[i] = max(profit_without_curr, profit_with_curr)

        return dp_max_profit[n - 1]

        # Time and Space Complexity:
        # Time Complexity: O(n log n)

        # Sorting: O(n log n)
        # For each job, binary search: O(log n)
        # Total: O(n log n)

        # Space Complexity: O(n)

        # DP array: O(n)
        # Jobs array: O(n)
        # Total: O(n)

        # ! sol2: recursion with memo
        n = len(startTime)
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda x: x[1])

        memo = {}

        def find_next_job(curr_idx: int) -> int:
            """Find the next job that doesn't overlap with current job."""
            curr_end = jobs[curr_idx][1]

            # left bound search for the first job that starts >= curr_end
            l, r = curr_idx + 1, n
            while l <= r:
                mid = (l + r) // 2
                if jobs[mid][0] >= curr_end:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def dp(idx: int) -> int:
            """return max profix starting from job idx."""
            if idx >= n:
                return 0

            if idx in memo:
                return memo[idx]

            # option 1: skip current job
            skip_profit = dp(idx + 1)

            # option2: take current job
            next_job_idx = find_next_job(idx)
            take_profit = jobs[idx][2] + dp(next_job_idx)

            memo[idx] = max(skip_profit, take_profit)

            return memo[idx]

        return dp(0)


# @lc code=end


#
# @lcpr case=start
# [1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,6]\n[3,5,10,6,9]\n[20,20,100,70,60]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n[2,3,4]\n[5,6,4]\n
# @lcpr case=end

#
