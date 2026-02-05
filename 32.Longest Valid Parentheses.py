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
        parentheses, length, valid parentheses, substring

        * pattern keywords
        stack

        * constraints
        well-formed, longest, substring (must be of the parent string)
        """
        if len(s) == 0:
            return 0

        longest = 0

        OPEN = "("
        CLOSED = ")"

        # when finalized, clean up the stack and update longest.

        stack: list[str] = []
        is_open = False
        for p in s:
            if not is_open and p == OPEN:
                is_open = True
                stack.append(p)
                continue

            if is_open and p == CLOSED:
                is_open = False
                stack.append(p)

            longest = max(longest, len(stack))

        return longest


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
