#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        # prefill
        ans = [[0] * n for _ in range(n)]

        # border indexes
        top, right, bottom, left = 0, n - 1, n - 1, 0

        # initial coordination
        (x, y) = (0, 0)

        # set coordination changes by  → ↓ ← ↑
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # 0: →, 1: ↓, 2: ← 3: ↑
        direction = 0

        for i in range(1, n ** 2 + 1):
            ans[y][x] = i

            # going right until reaching right border
            if direction == 0 and x == right:
                direction += 1
                top += 1
            # going down until reaching bottom border
            elif direction == 1 and y == bottom:
                direction += 1
                right -= 1
            # going left until reaching left border
            elif direction == 2 and x == left:
                direction += 1
                bottom -= 1
            # going up until reaching top border
            elif direction == 3 and y == top:
                direction += 1
                left += 1

            direction %= 4

            x, y = tuple(map(sum, zip((x, y), movements[direction])))

        return ans


# @lc code=end

