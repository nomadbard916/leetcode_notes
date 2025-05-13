#
# @lc app=leetcode id=652 lang=python3
# @lcpr version=30104
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        # 如果你想知道以自己为根的子树是不是重复的，是否应该被加入结果列表中，你需要知道什么信息？
        # 你需要知道以下两点：
        # 1、以我为根的这棵二叉树（子树）长啥样？
        # 2、以其他节点为根的子树都长啥样？
        # 我要知道以自己为根的子树长啥样，是不是得先知道我的左右子树长啥样，再加上自己，就构成了整棵子树的样子？
        # 左右子树的样子，可不就得在后序位置通过递归函数的返回值传递回来吗？
        # 我知道了自己长啥样，怎么知道别人长啥样？这样我才能知道有没有其他子树跟我重复对吧。
        # 这很简单呀，我们借助一个外部数据结构，让每个节点把自己子树的序列化结果存进去，
        # 这样，对于每个节点，不就可以知道有没有其他节点的子树和自己重复了么？
        # to get subtree info to compare => post order
        # to compare subtree structure and value => serialization
        res = []

        subtree_seen_times_dict = defaultdict(int)

        def recursive_serialize(root):
            if root is None:
                return "#"

            left_subtree = recursive_serialize(root.left)
            right_subtree = recursive_serialize(root.right)

            # *post order operations
            curr_subtree = f"{left_subtree},{right_subtree},{root.val}"

            subtree_seen_times = subtree_seen_times_dict[curr_subtree]
            # if duplicate, only need to return one of them
            if subtree_seen_times == 1:
                res.append(root)

            subtree_seen_times_dict[curr_subtree] = subtree_seen_times + 1

            return curr_subtree

        recursive_serialize(root)
        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,null,2,4,null,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,3,null,3,null]\n
# @lcpr case=end

#
