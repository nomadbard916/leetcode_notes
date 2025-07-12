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
        children_mapping: Dict[int, List[int]] = defaultdict(list)
        for i in range(n):
            curr_node_parent_val = parents[i]
            if curr_node_parent_val != -1:
                children_list = children_mapping[curr_node_parent_val]
                children_list.append(i)

        # * calculate subtree sizes for each node using DFS
        subtree_sizes = [0] * n

        def calculate_subtree_size(node: int) -> int:
            size = 1  # count the root itself
            for child in children_mapping[node]:
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

            child_subtree_sizes = []
            for child in children_mapping[node]:
                child_subtree_size = subtree_sizes[child]
                child_subtree_sizes.append(child_subtree_size)

            # * score calculation by components
            # consider children only
            for child_size in child_subtree_sizes:
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
