#
# @lc app=leetcode id=239 lang=python3
# @lcpr version=30201
#
# [239] Sliding Window Maximum
#

# @lc code=start
import heapq
from collections import deque
from typing import Deque, List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # The Key Idea: Monotonic Deque
        # A monotonic deque is a deque where elements are arranged in a specific order (increasing or decreasing).
        # Here we use a decreasing monotonic deque.

        # Why does this work?
        # 1. We store indices, not values - This helps us track whether elements are still within the current window
        # 2. Decreasing order property: If we have elements A and B where:
        # - A comes before B (A's index < B's index)
        # - A's value < B's value
        # - Then A can NEVER be the maximum while B is still in the window!
        # So we remove A from consideration.
        # 3. Front element is always maximum: Because we maintain decreasing order,
        # the front of the deque always contains the index of the maximum element in the current window.

        if not nums or k == 0:
            return []

        #  Deque stores indices of elements in decreasing order of their values
        dq: Deque[int] = deque()
        res = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            # The window is [i - k + 1, i], so we remove indices < i - k + 1
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Maintain decreasing order in deque
            # Remove elements from the back that are smaller than current element
            # Because they will never be the maximum while current element is in window
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current element's index to deque
            dq.append(i)

            # The front of deque always contains the index of maximum element
            # Start adding to result once we start to have a complete window (i >= k - 1)
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

        # Time Complexity: O(n)
        # Each element is added to the deque exactly once: O(n)
        # Each element is removed from the deque at most once: O(n)
        # Total: O(n)

        # Space Complexity: O(k)
        # The deque stores at most k elements (the window size)
        # The result array is O(n - k + 1), but that's for output, not counting towards auxiliary space

        # ! sol2: max heap
        result = []
        heap = []  # max heap (use negative values)

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            # Remove elements outside window
            while heap and heap[0][1] < i - k + 1:
                heapq.heappop(heap)

            if i >= k - 1:
                result.append(-heap[0][0])

        return result

        # Time: O(n log n) - heap operations
        # Space: O(n)
        # Better than brute force but not optimal


# @lc code=end


#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#
