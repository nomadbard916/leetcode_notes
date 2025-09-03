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
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(node: Optional[TreeNode]) -> None:
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                # Use "#" to represent null nodes
                vals.append("#")

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
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build_tree()  # Recursively build left subtree
            node.right = build_tree()  # Recursively build right subtree
            return node

        vals_iter = iter(data.split(","))
        return build_tree()


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
