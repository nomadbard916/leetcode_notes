# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def traverse(self, head: ListNode) -> ListNode:
        # use a dummy node as outside watcher.
        # the resulting linked list should be dummy_node.next as it points to the newly produced head
        dummy_node = ListNode()
        # in most scenarios, using previous node then defer current is better than using current node directly when there needs a dummy node as outside watcher
        prev_node = dummy_node

        # set some pre-condition before entering loop, eg. carry = 0

        while head:
            # move from previous node to currently traversed node
            prev_node.next = head

            # do some manipulation  on current node

            # after manipulation's done, we can prepare to move to next node
            head = head.next
            # remember to assign the already processed current node as the new previous node
            prev_node = prev_node.next

        # if there's two linked lists, remember to consider when l1 is None and/or l2 is None. do the while loop again for remaining nodes

        return dummy_node.next
