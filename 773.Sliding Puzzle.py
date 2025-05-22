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

        # the 2 x 3 matrix is always flattened as a one-dimensional string in later operations
        target = "123450"

        # convert a 2x3 matrix to string to be the starting point of BFS,
        # so it could be added to set
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

        steps = 0
        while q:
            q_size = len(q)
            for _ in range(q_size):
                cur_state = q.popleft()
                # check if it's reached the target state
                if cur_state == target:
                    return steps
                # swap number 0 with the neighboring number
                for state in self.get_state_transitions(cur_state):
                    # prevent visiting visited
                    if state not in visited:
                        q.append(state)
                        visited.add(state)
            steps += 1
        return -1

    def get_state_transitions(self, cur_state: str):
        # record the neighboring indexes for the matrix flattened as one-dimensional string
        neighbor_indexes_mapping = [
            [1, 3],
            [0, 4, 2],
            [1, 5],
            [0, 4],
            [3, 1, 5],
            [4, 2],
        ]
        movable_block = "0"
        movable_index = cur_state.index(movable_block)
        states = []
        for adj_block_index in neighbor_indexes_mapping[movable_index]:
            new_state = self.swap(cur_state, movable_index, adj_block_index)
            states.append(new_state)
        return states

    def swap(self, state: str, i: int, j: int) -> str:
        """
        Swap the characters at positions i and j in the board string,
        representing the moving of the physical block.


        Returns:
            str: The board string with the characters at positions i and j swapped.
        """
        chars = list(state)
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
