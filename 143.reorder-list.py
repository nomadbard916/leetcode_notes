#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # previous half goes forward, latter half backward,
        # then concat two iteratively

        # sanity check:  length of list should be >= 3
        if head is None or head.next is None or head.next.next is None:
            return head

        # find mid and cut list from half
        fast = slow = head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        head1, head2 = head, slow.next
        slow.next = None

        # reverse latter half list with head2
        dummy = ListNode()
        dummy.next = head2

        # manually deal with head2, which must be None
        current_head = head2.next
        head2.next = None

        while current_head:
            next_node = current_head.next
            previous_head = dummy.next

            current_head.next, dummy.next = previous_head, current_head

            current_head = next_node

        head2 = dummy.next

        #  merge two lined list head1 and head2
        p1, p2 = head1, head2

        while p2:
            temp1, temp2 = p1.next, p2.next

            p1.next, p2.next = p2, temp1
            p1, p2 = temp1, temp2

        # not a feasible solution
        # but it's good example why list may not be a good container for this solution:
        # original head cannot be found

        # container = []
        # current_node = head
        # while current_node:
        #     container.append(current_node)
        #     current_node = current_node.next

        # length = len(container)
        # if length <= 2:
        #     return head

        # mid_index = length // 2

        # first_half = container[:mid_index]
        # second_half = container[mid_index::-1]

        # prev = dummy = ListNode()
        # dummy.next = head

        # while first_half:
        #     f_node = first_half.pop(0)

        #     s_node = second_half.pop(0) if second_half else None

        #     prev.next = f_node
        #     f_node.next = s_node

        #     prev = s_node

        # return dummy.next


# @lc code=end

