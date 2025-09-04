#
# @lc app=leetcode id=297 lang=python3
# @lcpr version=30201
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

# ! don't uncomment it or it'll error
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    # it's essentially try to traverse the tree,
    # build the string, and recover the string using the same traversal method
    NULL_NODE_CHAR = "#"

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 即便你包含了空指针的信息，也只有前序和后序的遍历结果才能唯一还原二叉树，中序遍历结果做不到

        def preorder(node: Optional[TreeNode]) -> None:
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append(self.NULL_NODE_CHAR)

        vals = []
        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def build_tree() -> Optional[TreeNode]:
            val = next(vals_iter)
            if val == self.NULL_NODE_CHAR:
                return None
            node = TreeNode(int(val))
            node.left = build_tree()  # Recursively build left subtree
            node.right = build_tree()  # Recursively build right subtree
            return node

        vals_iter = iter(data.split(","))
        return build_tree()

        # Complexity Analysis
        # Time Complexity: O(n) where n is the number of nodes

        # Serialization: Visit each node exactly once
        # Deserialization: Process each value in the string exactly once

        # Space Complexity: O(n)

        # Serialization: O(n) for the result string + O(h) recursion stack where h is tree height
        # Deserialization: O(h) recursion stack space
        # In worst case (skewed tree), h = n, so O(n) total


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end


#
# @lcpr case=start
# [1,2,3,null,null,4,5]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
