#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        def generateTreesDFS(option_list={"left": 1, "right": n}):
            l_val = option_list["left"]
            r_val = option_list["right"]

            if l_val > r_val:
                return [None]

            # initialize child tree for current root
            tree = []

            for i in range(l_val, r_val + 1):
                left_nodes = generateTreesDFS({"left": l_val, "right": i - 1})
                right_nodes = generateTreesDFS({"left": i + 1, "right": r_val})

                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node

                        tree.append(root)

            return tree

        return generateTreesDFS()

        # sol2, shortened version of above solution
        # def newTree(x, l, r):
        #     t = TreeNode(x)
        #     t.left = l
        #     t.right = r
        #     return t

        # def genDFS(start, end):
        #     return [
        #         newTree(i, l, r)
        #         for i in range(start, end + 1)
        #         for l in genDFS(start, i - 1)
        #         for r in genDFS(i + 1, end)
        #     ] or [None]

        # return genDFS(1, n) if n > 0 else []


# @lc code=end

