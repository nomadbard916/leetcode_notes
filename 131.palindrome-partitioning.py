# @before-stub-for-debug-begin

# @before-stub-for-debug-end

#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#


# @lc code=start
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # partition -> slicing using separator index to separate 'checked' part and 'checkable' part, including every element
        # don't consider checked elements
        # palindrome ->two pointer, or reverse (with slicing syntax sugar)
        # the first element itself must be palindrome, therefore elements count must be >=1

        ans = []

        # sanity check
        if len(s) < 1:
            return ans

        def is_palindrome(string: str):
            return string == string[::-1]

        def backtrack(current_path: list, option_list=s):
            option_length = len(option_list)

            # ending condition: the option list is all partitioned, ie option_length== 0
            if option_length == 0:
                ans.append(current_path)
                return

            # as the first element itself must be palindrome
            # and slicing/range() doesn't contain right bound
            # therefore the range should be manipulated more meticulously
            for i in range(1, option_length + 1):
                checking = option_list[:i]
                checkable = option_list[i:]

                if is_palindrome(checking):
                    updated_path = current_path + [checking]

                    # checkable will be '' when i reaches option_length
                    backtrack(updated_path, checkable)

        current_path = []
        backtrack(current_path)

        return ans


# @lc code=end
