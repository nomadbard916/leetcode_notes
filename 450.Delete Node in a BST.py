#
# @lc app=leetcode id=450 lang=python3
# @lcpr version=30104
#
# [450] Delete Node in a BST
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
    def getMin(self, node: TreeNode) -> TreeNode:
        # BST 最左边的就是最小的
        while node.left is not None:
            node = node.left
        return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # root.val == key
        else:
            # 找到目标节点了，比方说是节点 A，如何删除这个节点，这是难点。因为删除节点的同时不能破坏 BST 的性质。有三种情况
            # 情况 1：A 恰好是末端节点，两个子节点都为空，那么它可以当场去世了。
            # 情况 2：A 只有一个非空子节点，那么它要让这个孩子接替自己的位置。
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # 情况 3：A 有两个子节点，麻烦了，为了不破坏 BST 的性质，A 必须找到左子树中最大的那个节点，或者右子树中最小的那个节点来接替自己。我们以第二种方式讲解。
            minNode = self.getMin(root.right)
            # 删除右子树最小的节点
            root.right = self.deleteNode(root.right, minNode.val)
            # 用右子树最小的节点替换 root 节点
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        return root


# @lc code=end


#
# @lcpr case=start
# [5,3,6,2,4,null,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [5,3,6,2,4,null,7]\n0\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
