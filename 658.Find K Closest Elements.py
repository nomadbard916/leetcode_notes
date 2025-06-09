#
# @lc app=leetcode id=658 lang=python3
# @lcpr version=30104
#
# [658] Find K Closest Elements
#

# @lc code=start
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Find the k closest elements to x in a sorted array.

        Approach: Two Pointers (Sliding Window)
        - Use left and right pointers to maintain a window of size k
        - Compare distances from window boundaries to x
        - Shrink window by removing the element farther from x

        Time Complexity: O(n - k) where n is length of arr
        Space Complexity: O(1) excluding output space
        """
        # ! sol1: just sliding window
        l = 0
        r = len(arr) - 1

        # * shrink window until we have exactly k elements
        while r - l + 1 > k:
            # Compare distances of leftmost and rightmost elements to x
            if abs(arr[l] - x) > abs(arr[r] - x):
                # Left element is farther, remove it
                l += 1
            else:
                # Right element is farther or equal distance, remove it
                # We prefer smaller values when distances are equal
                r -= 1
        # Return the k elements in the final window
        return arr[l : r + 1]

        """
        Alternative approach using Binary Search to find optimal starting position.

        Time Complexity: O(log(n-k) + k) where n is length of arr
        Space Complexity: O(1) excluding output space
        """
        # ! sol2: only binary search
        left = 0
        right = len(arr) - k

        # Binary search for the best starting position
        while left < right:
            mid = (left + right) // 2

            # Compare distances of elements at positions mid and mid+k
            if x - arr[mid] > arr[mid + k] - x:
                # The element at mid+k is closer, search right half
                left = mid + 1
            else:
                # The element at mid is closer or equal, search left half
                right = mid

        # Return k elements starting from the optimal position
        return arr[left : left + k]

        # ! sol3: binary search + two pointers from center... but it's only showing off the left-bound framework
        # * by the condition |a - x| == |b - x| and a < b => it must be left bound
        def left_bound_binary_search(nums: List[int], target: int):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return left

        # * two pointers from center
        res = []
        x_idx = left_bound_binary_search(arr, x)
        # range: (left, right)
        # both could be out of bound, so careful when putting res
        left, right = x_idx - 1, x_idx
        # expand until there are k elements included
        while right - left - 1 < k:
            # left out of bound, there's no elements on the left side to consider
            if left == -1:
                right += 1
            # right out of bound, there's no elements on the right side to consider
            elif right == len(arr):
                left -= 1
            # if there's room for expending on both sides
            # left farther away from x then right, so expand right to include the closer value
            elif abs(arr[left] - x) > abs(arr[right] - x):
                right += 1
            else:
                left -= 1
        for i in range(left + 1, right):
            res.append(arr[i])
        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n4\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,4,5]\n4\n-1\n
# @lcpr case=end

#
