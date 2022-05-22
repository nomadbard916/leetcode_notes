#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s, stack_t = [], []
        for s_char in s:
            if s_char != "#":
                stack_s.append(s_char)
            elif stack_s:
                stack_s.pop()

        for t_char in t:
            if t_char != "#":
                stack_t.append(t_char)
            elif stack_t:
                stack_t.pop()

        return stack_s == stack_t


# @lc code=end
