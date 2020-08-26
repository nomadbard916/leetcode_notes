#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # it's indeed ok to use fast and slow nodes, but this method's too trivial
        # just turn the linked list to list and follow 108

        def solution_108(nums):
            length = len(nums)

            # sanity check
            if length == 0:
                return None
            if length == 1:
                return TreeNode(nums[0])

            mid = length // 2
            root = TreeNode(nums[mid])

            root.left = solution_108(nums[:mid])
            root.right = solution_108(nums[mid + 1 :])

            return root

        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        return solution_108(nums)


# @lc code=end

