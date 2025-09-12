#
# @lc app=leetcode id=621 lang=python3
# @lcpr version=30201
#
# [621] Task Scheduler
#

# @lc code=start
from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ! sol 1: Mathematical Formula (Optimal)
        # Key Insight: The bottleneck is always the most frequent task(s).

        task_freq_count = Counter(tasks)

        max_freq = max(task_freq_count.values())

        # count how many tasks have the max freq
        max_freq_count = sum(
            1 for count in task_freq_count.values() if count == max_freq
        )

        # calculate min time needed
        # formula: (max_freq -1) * (n+1) + max_freq_count
        # but it should be at least len(tasks)
        min_time = (max_freq - 1) * (n + 1) + max_freq_count

        return max(min_time, len(tasks))

        # complexities
        # Time: O(N) where N is number of tasks (for counting frequencies)
        # Space: O(1) since we have at most 26 different task types

        # ! col 2: Greedy Simulation with max heap
        """
        Alternative greedy approach using max heap simulation.
        This approach actually simulates the scheduling process.
        """
        # complexities
        # Time: O(N log 26) = O(N) since heap operations are on at most 26 elements
        # Space: O(1) for the same reason


# @lc code=end


#
# @lcpr case=start
# ["A","A","A","B","B","B"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["A","C","A","B","D","B"]\n1\n
# @lcpr case=end

# @lcpr case=start
# ["A","A","A", "B","B","B"]\n3\n
# @lcpr case=end

#
