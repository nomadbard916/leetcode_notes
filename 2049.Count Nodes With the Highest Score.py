#
# @lc app=leetcode id=2049 lang=python3
# @lcpr version=30201
#
# [2049] Count Nodes With the Highest Score
#

# @lc code=start
from collections import defaultdict
from typing import Dict, List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)

        # * build adjacency list representation of the tree as we are only having "parents" relationship array
        children: Dict[int, List[int]] = defaultdict(list)
        for i in range(n):
            if parents[i] != -1:
                children[parents[i]].append(i)

        # * calculate subtree sizes for each node using DFS
        subtree_sizes = [0] * n

        def calculate_subtree_size(node: int) -> int:
            size = 1  # count the root itself
            for child in children[node]:
                size += calculate_subtree_size(child)
            subtree_sizes[node] = size
            return size

        # start DFS from root (node 0)
        calculate_subtree_size(0)

        # * calculate score for each node
        max_score = 0
        max_count = 0

        for node in range(n):
            score = 1

            child_subtrees = [subtree_sizes[child] for child in children[node]]

            # score calculation, consider children only
            for child_size in child_subtrees:
                score *= child_size

            # consider parent levels
            remaining_size = n - subtree_sizes[node]
            if remaining_size > 0:
                score *= remaining_size

            # update global info
            if score > max_score:
                max_score = score
                max_count = 1
            elif score == max_score:
                max_count += 1

        return max_count


# @lc code=end


#
# @lcpr case=start
# [-1,2,0,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [-1,2,0]\n
# @lcpr case=end

#
