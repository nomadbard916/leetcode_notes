#
# @lc app=leetcode id=1339 lang=python3
# @lcpr version=30201
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        max_product = 0

        # ! sol1:
        # * step 1: calculate total sum of all nodes
        def calc_total_sum(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_total_sum = calc_total_sum(node.left)
            right_total_sum = calc_total_sum(node.right)

            return node.val + left_total_sum + right_total_sum

        total_sum = calc_total_sum(root)

        # * Step 2: For each subtree, calculate its sum and the product
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_product

            if not node:
                return 0

            # Calculate sum of current subtree
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # * post order logic
            current_subtree_sum = node.val + left_sum + right_sum

            # If we remove this subtree, the remaining tree has sum: total_sum - current_subtree_sum
            remaining_sum = total_sum - current_subtree_sum
            product = current_subtree_sum * remaining_sum
            max_product = max(product, max_product)

            return current_subtree_sum

        dfs(root)

        return max_product % MOD

        # ! sol2: optimize; it looks pretty much like prefix sum, to store sums in a DS and use them in one pass
        # * preprocessing phase
        # Similar to prefix sum array, stores cumulative sums
        subtree_sums = []

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Calculate sum of current subtree (like building prefix sum)
            current_sum = node.val + dfs(node.left) + dfs(node.right)
            subtree_sums.append(current_sum)
            return current_sum

        total_sum = dfs(root)

        # * query phase
        # check all possible splits (except the root itself)
        # This is like using prefix sum to get range sums efficiently
        # Key Insight: When we remove an edge, we're essentially separating a subtree from the rest of the tree.
        # If a subtree has sum S, then the remaining tree has sum total_sum - S.
        # exclude root, the last item, as it's post order
        for subtree_sum in subtree_sums[:-1]:
            remaining_sum = total_sum - subtree_sum  # Like total - prefix[i]
            product = subtree_sum * remaining_sum
            max_product = max(max_product, product)

        return max_product % MOD

        # Time and Space Complexity:

        # Time Complexity: O(n) where n is the number of nodes
        # We visit each node twice: once to calculate total sum, once to find optimal split

        # Space Complexity: O(h) where h is the height of the tree
        # Due to recursion stack depth


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,null,null,5,6]\n
# @lcpr case=end

#
