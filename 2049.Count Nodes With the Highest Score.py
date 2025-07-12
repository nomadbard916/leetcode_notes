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

            # * score calculation by components
            # consider children only
            for child_size in child_subtrees:
                score *= child_size

            # consider everything else that was connected through the parent
            remaining_size = n - subtree_sizes[node]
            if remaining_size > 0:
                score *= remaining_size

            # update global info
            # When score > max_score, it means we've found a new maximum score that's higher than any we've seen before,
            # so max resets to 1
            if score > max_score:
                max_score = score
                max_count = 1
            elif score == max_score:
                max_count += 1

        return max_count

        # Time and Space Complexity

        # Time Complexity: O(n) where n is the number of nodes
        # Building the tree: O(n)
        # DFS for subtree sizes: O(n) - visits each node once
        # Score calculation: O(n) - processes each node once
        # Total: O(n)

        # Space Complexity: O(n)
        # Children adjacency list: O(n)
        # Subtree sizes array: O(n)
        # DFS recursion stack: O(h) where h is tree height, worst case O(n)
        # Total: O(n)


# @lc code=end


#
# @lcpr case=start
# [-1,2,0,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [-1,2,0]\n
# @lcpr case=end

#
