#
# @lc app=leetcode id=773 lang=python3
# @lcpr version=30104
#
# [773] Sliding Puzzle
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # from init state to final state with as few state transitions as possible
        # ! => see it as BFS tree traversal with shortest path
        # * careful of visited node, or it might cause infinite circulation

        target = "123450"
        # convert a 2x3 matrix to string to be the starting point of BFS
        start = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                start += str(board[i][j])

        # ! BFS traversal with template
        q = deque()
        visited = set()
        # start BFS traversal from the starting point
        q.append(start)
        visited.add(start)

        step = 0
        while q:
            q_size = len(q)
            for _ in range(q_size):
                cur = q.popleft()
                # check if it's reached the target state
                if cur == target:
                    return step
                # swap number 0 with the neighboring number
                for neighboard_board in self.get_neighbors(cur):
                    # prevent visiting visited
                    if neighboard_board not in visited:
                        q.append(neighboard_board)
                        visited.add(neighboard_board)
            step += 1
        return -1

    def get_neighbors(self, board):
        # record the neighboring indexes for one-dimensional string
        mapping = [[1, 3], [0, 4, 2], [1, 5], [0, 4], [3, 1, 5], [4, 2]]
        idx = board.index("0")
        neighbors = []
        for adj in mapping[idx]:
            new_board = self.swap(board, idx, adj)
            neighbors.append(new_board)
        return neighbors

    def swap(self, board, i, j):
        chars = list(board)
        chars[i], chars[j] = chars[j], chars[i]
        return "".join(chars)


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,0,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,1,2],[5,0,3]]\n
# @lcpr case=end

#
