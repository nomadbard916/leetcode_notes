#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # easiest solution: flatten to 1 dimension, sort and just return index (k-1) for new matrix

        # binary search, bisect() is a feasible tool

        length = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        def search(mid):
            # start from lower left and look towards upper right
            i, j = length - 1, 0
            # count number of elements less than or equal to mid
            count = 0

            while i >= 0 and j < length:
                if matrix[i][j] <= mid:
                    # when the element is less than or equal to mid
                    # then all the elements above the element will be less than or equal to mid
                    count += i + 1
                    j += 1  # move right
                else:
                    # When the element is larger than mid, it means that the element is not included
                    i -= 1  # move up

            # Compare the value of count with the value of K to determine where the element is located
            return count >= k

        while left < right:
            mid = (left + right) // 2

            if search(mid):
                right = mid
            else:
                left = mid + 1

        return left

        # sol2: kth => heap


# @lc code=end

