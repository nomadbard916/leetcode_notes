#
# @lc app=leetcode id=752 lang=python3
# @lcpr version=30104
#
# [752] Open the Lock
#

# @lc code=start
import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # * it's essentially an 8-ary tree
        # e.g. starting from "0000", there are 8 possible state transitions:
        # 1000, 9000, 0100, 0900, ..., 0009, 0001
        # * while "visited" should be taken care of to avoid cyclic graph
        # * and we must be careful about "deadends"
        # => just put them into "visited" from the very beginning

        starting_point = "0000"
        deads_set = set(deadends)

        if starting_point in deads_set:
            return -1

        # to avoid graph circulation, and include deads from the very beginning
        visited_set = set(deadends)
        q = collections.deque()
        # begin BFS from starting point
        steps = 0
        q.append(starting_point)
        visited_set.add(starting_point)

        while q:
            q_size = len(q)
            # get all the neighbors of nodes in queue
            for _ in range(q_size):
                cur = q.popleft()

                if cur == target:
                    return steps

                # put all the valid neighbors into queue
                for neighbor in self.get_neighbors(cur):
                    if neighbor not in visited_set:
                        q.append(neighbor)
                        visited_set.add(neighbor)
            steps += 1
        return -1

    def plus_one(self, s: str, i: int) -> str:
        chars_list = list(s)
        curr_char = chars_list[i]
        if curr_char == "9":
            chars_list[i] = "0"
        else:
            new_char_order = ord(curr_char) + 1
            chars_list[i] = chr(new_char_order)
        return "".join(chars_list)

    def minus_one(self, s: str, i: int) -> str:
        chars_list = list(s)
        curr_char = chars_list[i]
        if curr_char == "0":
            chars_list[i] = "9"
        else:
            new_char_order = ord(curr_char) - 1
            chars_list[i] = chr(new_char_order)
        return "".join(chars_list)

    def get_neighbors(self, s: str) -> List[str]:
        neighbors = []
        # all the 8 possibilities. just put all the valid and invalid ones, do validation later.
        for i in range(4):
            neighbors.append(self.plus_one(s, i))
            neighbors.append(self.minus_one(s, i))
        return neighbors


# @lc code=end


#
# @lcpr case=start
# ["0201","0101","0102","1212","2002"]\n"0202"\n
# @lcpr case=end

# @lcpr case=start
# ["8888"]\n"0009"\n
# @lcpr case=end

# @lcpr case=start
# ["8887","8889","8878","8898","8788","8988","7888","9888"]\n"8888"\n
# @lcpr case=end

#
