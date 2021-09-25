#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # greedy
        # stack

        stack = []
        seen = set()
        # if same key, latter value overrides previous, therefore it can be called 'last'
        char_last_idx = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue

            # remove previous stacked characters
            # when current character is still less then the top of stack
            # and not first time appearance
            # while stack still not empty
            while stack and c < stack[-1] and i < char_last_idx[stack[-1]]:
                top_char_popped = stack.pop()
                seen.remove(top_char_popped)
            stack.append(c)
            # only after appended can we say a character is 'seen',
            # therefore it needs removed when popped
            seen.add(c)

        return "".join(stack)


# @lc code=end

