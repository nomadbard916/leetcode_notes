#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections


class Solution:
    def connect(self, root: "Node") -> "Node":
        # just like 116, but as it's not perfect BST and some nodes are missing
        # => BFS
        if not root:
            return

        queue = collections.deque([root])

        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                current_node = queue.popleft()
                # if it's not the last element in the layer
                if i != queue_len - 1:
                    current_node.next = queue[0]

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return root


# @lc code=end

