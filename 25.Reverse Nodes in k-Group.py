#
# @lc app=leetcode id=25 lang=python3
# @lcpr version=30201
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # nouns and verbs
        """
        head
        linked list
        reverse every group of k
        leave remainder as is
        modified list
        positive integer
        k-group

        change pointers
        """

        # pattern kws
        """
        linked list
        not alter - in place
        reverse
        dummy node
        prev, tail, next_group_start
        reverse sublist, head insertion, iterative reversal
        """

        # structural kws
        """
        positive integer
        not multiplier -> remain as is
        k at most 5000, relatively small
        val at most 1000, relatively small
        O(1) extra memory?

        """


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n3\n
# @lcpr case=end

#
