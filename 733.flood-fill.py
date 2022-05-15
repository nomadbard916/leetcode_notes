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
        LENGTH, WIDTH = len(image), len(image[0])
        color = image[sr][sc]

        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor

                if r >= 1:
                    dfs(r - 1, c)
                if r < LENGTH - 1:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c < WIDTH - 1:
                    dfs(r, c + 1)

        dfs(sr, sc)

        return image


# @lc code=end
