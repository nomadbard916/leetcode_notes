#
# @lc app=leetcode id=295 lang=python3
# @lcpr version=30201
#
# [295] Find Median from Data Stream
#

# @lc code=start
import heapq


class MedianFinder:
    # or we may use sorted list with binary search,
    # to insert number while keeping the list sorted.
    # less efficient but easier to understand.
    # complexities of addNum:
    #  Time Complexity: O(n) - insertion in sorted order
    # Space Complexity: O(n) - storing all numbers
    # complexities of findMedian:
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def __init__(self):
        # Python heapq is min heap by default
        # For max heap, we store negative values
        self.max_heap = []  # Left half (smaller numbers) - stores negative values
        self.min_heap = []  # Right half (larger numbers) - stores positive values

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.

        Algorithm:
        1. If max_heap is empty or num <= top of max_heap, add to max_heap
        2. Otherwise, add to min_heap
        3. Balance the heaps to maintain size invariant

        Time Complexity: O(log n) - heap operations
        Space Complexity: O(n) - storing all numbers
        """
        # Step 1: Add number to appropriate heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Step 2: Balance heaps
        # Ensure max_heap has at most 1 more element than min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move top element from max_heap to min_heap
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            # Move top element from min_heap to max_heap
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        """
        Find the median of all elements added so far.

        Time Complexity: O(1) - just accessing heap tops
        Space Complexity: O(1) - no additional space
        """
        if len(self.max_heap) > len(self.min_heap):
            # Odd number of elements, median is top of max_heap
            return float(-self.max_heap[0])
        else:
            # Even number of elements, median is average of both heap tops
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
