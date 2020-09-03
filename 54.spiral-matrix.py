#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # https://blog.csdn.net/fuxuemingzhu/article/details/79541501
        ans = []

        if not matrix or not matrix[0]:
            return ans

        M, N = len(matrix), len(matrix[0])

        # position index of borders
        left, right, top, bottom = 0, N - 1, 0, M - 1

        # set initial coordination
        (x, y) = (0, 0)

        # set coordination changes by  → ↓ ← ↑
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # 0: →, 1: ↓, 2: ← 3: ↑
        direction = 0

        while len(ans) != M * N:
            ans.append(matrix[y][x])

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
