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
        # median happens on midpoint between max of smaller and min of larger
        # Python heapq is min heap by default
        # For max heap, we store negative values
        self.smaller_max_heap = []  # Left half (smaller numbers) - stores negative values
        self.larger_min_heap = []  # Right half (larger numbers) - stores positive values

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
        if not self.smaller_max_heap or num <= -self.smaller_max_heap[0]:
            heapq.heappush(self.smaller_max_heap, -num)
        else:
            heapq.heappush(self.larger_min_heap, num)

        # Step 2: Balance heaps
        # Ensure max_heap has at most 1 more element than min_heap
        if len(self.smaller_max_heap) > len(self.larger_min_heap) + 1:
            # Move top element from max_heap to min_heap
            val = -heapq.heappop(self.smaller_max_heap)
            heapq.heappush(self.larger_min_heap, val)
        elif len(self.larger_min_heap) > len(self.smaller_max_heap):
            # Move top element from min_heap to max_heap
            val = heapq.heappop(self.larger_min_heap)
            heapq.heappush(self.smaller_max_heap, -val)

    def findMedian(self) -> float:
        """
        Find the median of all elements added so far.

        Time Complexity: O(1) - just accessing heap tops
        Space Complexity: O(1) - no additional space
        """
        if len(self.smaller_max_heap) > len(self.larger_min_heap):
            # Odd number of elements, median is top of max_heap
            return float(-self.smaller_max_heap[0])
        else:
            # Even number of elements, median is average of both heap tops
            return (-self.smaller_max_heap[0] + self.larger_min_heap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
