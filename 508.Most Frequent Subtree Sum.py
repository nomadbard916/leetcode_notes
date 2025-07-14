#
# @lc app=leetcode id=508 lang=python3
# @lcpr version=30201
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        sum_count_mapping: Dict[int, int] = defaultdict(int)

        def calculate_subtree_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_sum = calculate_subtree_sum(node.left)
            right_sum = calculate_subtree_sum(node.right)

            # * post order logic
            current_subtree_sum = node.val + left_sum + right_sum

            sum_count_mapping[current_subtree_sum] += 1

            return current_subtree_sum

        calculate_subtree_sum(root)

        max_frequency = max(sum_count_mapping.values())

        result = []

        # Return all sums that have maximum frequency
        for sum_val, frequency in sum_count_mapping.items():
            if frequency == max_frequency:
                result.append(sum_val)

        return result

    # Time and Space Complexity:
    # Time Complexity: O(n) where n is the number of nodes. We visit each node exactly once.
    # Space Complexity: O(n) for the recursion stack (worst case for skewed tree) plus O(n) for the frequency map in worst case where all subtree sums are unique.


# @lc code=end


#
# @lcpr case=start
# [5,2,-3]\n
# @lcpr case=end

# @lcpr case=start
# [5,2,-5]\n
# @lcpr case=end

#
