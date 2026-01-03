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
        linked list
        reverse every group of k
        * leave remainder as is
        """

        # pattern kws
        """
        linked list
        not alter - in place
        reverse
        * k-group - fixed size chunks, need counter for tracking group boundaries
        dummy node
        prev, tail, next_group_start
        reverse sublist, head insertion, iterative reversal
        """

        # structural kws
        """
        * exactly k nodes -> group size validation
        less than k nodes -> edge case handling
        positive integer
        not multiplier -> remain as is
        k at most 5000, relatively small
        val at most 1000, relatively small
        O(1) extra memory?

        """

        # mental categories
        """
        linked list manipulation
        """

        # build solution from keywords
        """
        * think of "reverse linked list" first, than add layers of orchestration
        1. use dummy node to handle edge cases
        2. count or look-ahead to verify k nodes exist
        3. reverse k nodes using standard reversal pattern
        4. connect reversed group back to main list
        5. move pointers to next group
        6. repeat until insufficient nodes remain
        """

        # ! sol1: iterative
        def get_kth_node(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        # Edge case: if k is 1 or list is empty, no change needed
        if not head or k == 1:
            return head

        # Use dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head

        # * for non-traversal nodes, essentially these should be anchored.
        # - for the group to be traversed: start and end
        # - the node right before the traversal group
        # - the node right after the traversal group

        # Anchor 1: node right before the group
        prev_group_end = dummy

        while True:
            # Step 1: Record anchor nodes and check if we have k nodes remaining
            group_start = prev_group_end.next  # Anchor 2
            group_end = get_kth_node(prev_group_end, k)  # Anchor 3
            # If we don't have k nodes, we're done
            if not group_end:
                break

            # Step 2: Save the start of next group as anchor
            next_group_start = group_end.next  # Anchor 4

            # Step 3: Reverse the current group
            # We need to reverse from prev_group_end.next to kth_node (inclusive)
            prev, curr = next_group_start, group_start

            # * Standard reversal pattern for k nodes
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 4: Connect the reversed group back to the main list using anchors
            prev_group_end.next = group_end  # Anchor 1 -> Anchor 3
            # group_start.next is already pointing to next_group_start from reversal
            # Move Anchor 1 for next iteration
            prev_group_end = group_start

        return dummy.next

        # ! sol2 : iterative
        """
        Recursive approach to reverse k-group.
        More elegant but uses O(n/k) call stack space.
        """

        def reverseLinkedList(self, head: ListNode, k: int) -> ListNode:
            """Reverse first k nodes of a linked list."""
            prev = None
            curr = head

            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1

            return prev

        # Count if we have k nodes
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        # If we have k nodes, reverse them
        if count == k:
            # Reverse first k nodes
            reversed_head = self.reverseLinkedList(head, k)

            # head is now the tail of reversed group
            # curr is the start of next group
            # Recursively reverse next groups
            head.next = self.reverseKGroup(curr, k)

            return reversed_head

        # Less than k nodes remaining, return as is
        return head

        ## Complexity Analysis
        # - **Time Complexity**: O(n), where n is the number of nodes
        # - We visit each node exactly once
        # - The getKthNode() helper moves forward k steps per group
        # - Total operations: n (for reversal) + n (for look-ahead) = O(n)

        # - **Space Complexity**: O(1)
        # - Only using a fixed number of pointers
        # - No extra data structures

        """
        ## Extended Learning Ideas

        ### 1. **Why This Problem is Important**

        This problem teaches you:
        - **Multi-pointer technique**: Managing 4-5 pointers simultaneously
        - **State machine thinking**: Tracking where you are in the process
        - **Edge case handling**: Empty list, k=1, single group, etc.
        - **Modular design**: Breaking down complex operations (verify → reverse → connect)

        ### 2. **Variations to Practice**

        Try modifying the problem:
        - **Reverse alternate k groups**: Reverse 1st group, skip 2nd, reverse 3rd, etc.
        - **Reverse last k nodes**: Only reverse the last group if it has k nodes
        - **Reverse with m and n**: Reverse m nodes, skip n nodes, repeat

        ### 3. **Common Mistakes**

        - **Forgetting to check for k nodes**: Reversing without verification
        - **Losing connection**: Not properly reconnecting reversed group
        - **Off-by-one errors**: Miscounting k nodes
        - **Modifying head without dummy**: Makes edge cases harder

        ### 4. **Debugging Technique**

        For linked list problems, always **draw it out**:
        ```
        Step 1: [dummy] -> 1 -> 2 -> 3 -> 4 -> 5
                        ^              ^
                    prev_group_end    kth_node

        Step 2: After reversal
        [dummy] -> 2 -> 1 -> 3 -> 4 -> 5
                        ^
                prev_group_end (moved)

        One More Thing: The Pattern Generalizes
        This "4 anchor points" pattern appears in many linked list problems:

        - Reverse between positions m and n → Same 4 anchors
        - Remove nth node from end → Need anchor before it
        - Rotate list → Need to find cut points (anchors)
        - Reorder list → Find middle (anchor) and reconnect

        So you've just learned a transferable mental model! 🎉
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
