#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        # comare with 200
        LENGTH, WIDTH = len(image), len(image[0])

        curr_color = image[sr][sc]

        if curr_color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] != curr_color:
                return

            image[r][c] = newColor

            upper_index = r - 1
            lower_index = r + 1
            left_index = c - 1
            right_index = c + 1
            if r >= 1:
                dfs(upper_index, c)
            if r < LENGTH - 1:
                dfs(lower_index, c)
            if c >= 1:
                dfs(r, left_index)
            if c < WIDTH - 1:
                dfs(r, right_index)

        dfs(sr, sc)

        return image


# @lc code=end
