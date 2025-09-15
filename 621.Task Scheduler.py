#
# @lc app=leetcode id=621 lang=python3
# @lcpr version=30201
#
# [621] Task Scheduler
#

# @lc code=start
import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ! col 1: Greedy Simulation with max heap
        """
        Greedy approach using max heap simulation.
        This approach actually simulates the scheduling process.
        The greedy choice is always to execute the task with largest remaining frequency
        (to avoid it creating many future forced idles).
        """
        if n == 0:
            return len(tasks)

        # Count frequencies
        task_freq_count = Counter(tasks)

        # Use max heap (negate values for min heap in Python)
        max_heap = [-count for count in task_freq_count.values()]
        heapq.heapify(max_heap)

        time = 0

        while max_heap:
            # Store tasks that are in cooling period
            temp = []
            tasks_done = 0

            # Try to schedule n+1 tasks (including current time slot) in a box, then fill in box by box
            for _ in range(n + 1):
                if max_heap:
                    tasks_done += 1
                    # Get most frequent task
                    freq = heapq.heappop(max_heap)
                    # If still has remaining tasks after this execution
                    # If freq == -1 that means there was exactly 1 remaining before execution;
                    # after executing there are 0 left, so you must NOT push it back.
                    if freq < -1:  # freq is negative, so -1 means originally 1
                        temp.append(freq + 1)  # Decrease frequency

            # Put back tasks that still need to be executed with freq already decreased
            for freq in temp:
                heapq.heappush(max_heap, freq)

            # If heap is empty, we've scheduled all tasks
            # Add only the actual tasks scheduled, not idle time
            if not max_heap:
                # it's always less than n + 1
                time += tasks_done
                break
            else:
                # Full cycle completed (n+1 time units)
                time += n + 1

        return time

        # complexities
        # Time: O(N log 26) = O(N) since heap operations are on at most 26 elements
        # Space: O(1) for the same reason

        # ! sol 2: Mathematical Formula (Optimal, but too specific for this problem only)
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
