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
        # ! sol1: find the smallest head node in lists first => using heap
        # Why this works: The heap always gives us the globally smallest unprocessed element,
        # ensuring the result stays sorted.
        if not lists or len(lists) == 0:
            return None

        min_heap = []

        for list_idx, head in enumerate(lists):
            if head:
                # list_idx is not actually used in logic,
                # but it's still needed for identifying nodes
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

        # complexities
        # - Time: O(N × log k) where N = total nodes, k = number of lists
        # We process each node once (N operations)
        # Each heap operation takes O(log k) time
        # - Space: O(k) for the heap

        # ! sol2: divide and conquer
        # Core Idea: Recursively merge lists in pairs until only one list remains.
        if not lists or len(lists) == 0:
            return None

        def mergeTwoLists(
            l1: Optional[ListNode], l2: Optional[ListNode]
        ) -> Optional[ListNode]:
            dummy = ListNode()
            current = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next

            current.next = l1 or l2

            return dummy.next

        while len(lists) > 1:
            merged_lists = []

            # merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                merged_lists.append(mergeTwoLists(l1, l2))
            lists = merged_lists
        return lists[0]

        # complexities
        # - Time: O(N × log k)
        # log k levels of merging
        # Each level processes all N nodes once
        # - Space: O(log k) for recursion stack


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
