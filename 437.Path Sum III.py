#
# @lc app=leetcode id=437 lang=python3
# @lcpr version=30104
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # of course we can do brute force, but
        # time complexity O(n square), space complexity O(h)

        # The brilliance of prefix sum approach is that it turns a potentially
        # O(n²) problem into an O(n) solution by using memory (the prefix sum dictionary)
        # to avoid redundant calculations.

        # prefix sums encountered in current path
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # Initialize with 0 sum having frequency 1

        def dfs(root, curr_sum):
            count = 0
            if not root:
                return count

            # * preorder traversal
            curr_sum += root.val
            # Check if there's a prefix sum that can be subtracted to get targetSum
            # This count gives us the number of valid paths ending at current node
            count = prefix_sum_count[curr_sum - targetSum]

            # Update prefix sum frequency
            prefix_sum_count[curr_sum] += 1

            # Continue DFS on left and right children
            count += dfs(root.left, curr_sum)
            count += dfs(root.right, curr_sum)

            # ! Backtrack: remove current node's contribution to prefix sum
            # Why We Need Backtracking
            # In this problem, we are only interested in downward paths (parent to child).
            # Without backtracking, we would count invalid paths that go up and then down the tree.
            prefix_sum_count[curr_sum] -= 1

            return count

        return dfs(root, 0)

        # Time Complexity: O(n) where n is the number of nodes, as we visit each node exactly once.
        # Space Complexity: O(n) in the worst case for the dictionary (if all prefix sums are unique),
        # plus O(h) for the recursion stack where h is the height of the tree.

        # sol 2: we can still know about brute force, just in case and for thinking...
        # Base case: empty tree
        if not root:
            return 0

        # Count paths starting from the root
        def count_paths(self, node, remaining_sum):
            # Base case: empty node
            if not node:
                return 0

            # Initialize count
            count = 0

            # Check if current node value equals remaining sum
            if node.val == remaining_sum:
                count += 1

            # Continue path to children with updated remaining sum
            count += self.count_paths(node.left, remaining_sum - node.val)
            count += self.count_paths(node.right, remaining_sum - node.val)

            return count

        paths_from_root = count_paths(root, targetSum)

        # Recursively count paths starting from left and right children
        paths_from_left = self.pathSum(root.left, targetSum)
        paths_from_right = self.pathSum(root.right, targetSum)

        # Return total count
        return paths_from_root + paths_from_left + paths_from_right

        # Time Complexity: O(n²) in the worst case. For each node, we might need to traverse all its descendants, which could be O(n) nodes. Since there are n nodes, the overall complexity is O(n²).
        # Space Complexity: O(h) where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this could be O(n).


# @lc code=end


#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#
