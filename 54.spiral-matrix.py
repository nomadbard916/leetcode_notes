#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # https://blog.csdn.net/fuxuemingzhu/article/details/79541501
        ans = []

        if not matrix or not matrix[0]:
            return ans

        H, W = len(matrix), len(matrix[0])

        # position index of borders
        l_border, r_border, top_border, btm_border = 0, W - 1, 0, H - 1

        # set initial coordination
        (x, y) = (0, 0)

        # set coordination changes by  → ↓ ← ↑
        MOVEMENTS = {"right": (1, 0), "down": (0, 1), "left": (-1, 0), "up": (0, -1)}

        direction = "right"

        while len(ans) != H * W:
            ans.append(matrix[y][x])

            # going right until reaching right border
            if direction == "right" and x == r_border:
                direction = "down"
                top_border += 1
            # going down until reaching bottom border
            elif direction == "down" and y == btm_border:
                direction = "left"
                r_border -= 1
            # going left until reaching left border
            elif direction == "left" and x == l_border:
                direction = "up"
                btm_border -= 1
            # going up until reaching top border
            elif direction == "up" and y == top_border:
                direction = "right"
                l_border += 1

            x, y = (x + MOVEMENTS[direction][0], y + MOVEMENTS[direction][1])

        return ans


# @lc code=end
