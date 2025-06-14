#
# @lc app=leetcode id=23 lang=python3
# @lcpr version=30104
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # find the smallest head node in lists first => using heap
        min_heap = []

        for list_idx, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, list_idx, head))

        dummy = ListNode()
        current = dummy

        while min_heap:
            _, list_idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, list_idx, node.next))

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#
