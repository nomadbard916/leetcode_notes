#
# @lc app=leetcode id=32 lang=python3
# @lcpr version=30305
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        * nouns and verbs
        parentheses, length, valid, substring

        * pattern keywords
        stack
        longest substring: dynamic programming, sliding window

        * constraints
        well-formed, longest, substring (must be of the parent string)

        * tricky keywords:
        substring: must be contiguous
        longest: need to track max across all possibilities

        * mental categories:
        stack based matching
        dynamic programming
        two-pass scanning
        """
        # ! sol1: stack with index recording
        """
        Approach 2: Stack (Most Intuitive)
        Time: O(n), Space: O(n)

        Intuition: Use stack to track indices of unmatched characters.
        The distance between unmatched positions gives valid length.
        """
        # init with base for length calculation
        stack = [-1]
        max_len = 0
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
                continue

            # * char == ')'
            # try to match
            stack.pop()

            if not stack:
                # No matching '(', this ')' becomes new base
                stack.append(i)
                continue

            # Valid match found, calculate length
            # Current index - index of last unmatched character
            max_len = max(max_len, i - stack[-1])

        return max_len

        #  Why you got stuck
        # Your code uses a boolean (is_open) and a stack of characters, then measures len(stack) for the answer. That fails because:

        # A single boolean can't remember multiple unmatched '(', so nested or non-alternating patterns break your logic.
        # Storing characters and using len(stack) doesn't give the substring length (you need indices to compute lengths reliably).
        # it breaks at "(()"  and "()(())"
        # if len(s) == 0:
        #     return 0

        # longest = 0

        # OPEN = "("
        # CLOSED = ")"

        # # when finalized, clean up the stack and update longest.

        # stack: list[str] = []
        # is_open = False
        # for p in s:
        #     if p == OPEN:
        #         is_open = True
        #         stack.append(p)
        #         continue

        #     if is_open and p == CLOSED:
        #         is_open = False
        #         stack.append(p)

        #     longest = max(longest, len(stack))

        # return longest


# @lc code=end


#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#
