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

        # prev_group_end: pointer to the last node of previous group
        prev_group_end = dummy

        while True:
            # Step 1: Check if we have k nodes remaining
            kth_node = get_kth_node(prev_group_end, k)

            # If we don't have k nodes, we're done
            if not kth_node:
                break

            # Step 2: Save the start of next group
            next_group_start = kth_node.next

            # Step 3: Reverse the current group
            # We need to reverse from prev_group_end.next to kth_node (inclusive)
            prev, curr = kth_node.next, prev_group_end.next

            # * Standard reversal pattern for k nodes
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 4: Connect the reversed group back to the main list
            # After reversal:
            # - 'prev' points to the new head of reversed group (was kth_node)
            # - 'prev_group_end.next' points to old head (now tail of reversed group)
            original_group_start = prev_group_end.next
            prev_group_end.next = kth_node  # Connect previous part to new head

            # Step 5: Move prev_group_end to the end of current reversed group
            # (which is the original starting node)
            prev_group_end = original_group_start

        return dummy.next

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
