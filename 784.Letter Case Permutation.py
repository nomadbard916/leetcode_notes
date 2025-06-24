#
# @lc app=leetcode id=784 lang=python3
# @lcpr version=30104
#
# [784] Letter Case Permutation
#

# @lc code=start
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(index: int, current_path: List[str]):
            # * ending condition: if we've processed all characters
            if index == len(s):
                result.append("".join(current_path))
                return

            char = s[index]

            # for letters, try both lowercase and uppercase
            if char.isalpha():
                #  try lowercase version
                current_path.append(char.lower())
                backtrack(index + 1, current_path)
                current_path.pop()

                # try uppercase version
                current_path.append(char.upper())
                backtrack(index + 1, current_path)
                current_path.pop()

            # for digits, keep as is
            else:
                current_path.append(char)
                backtrack(index + 1, current_path)
                current_path.pop()

        backtrack(0, [])
        return result

        # Key Differences in Space Complexity:
        # Backtracking: Has additional O(n) space for the recursion call stack
        # Iterative: No recursion overhead, but uses O(m) temporary space per iteration

        # Why Both Have Same Time Complexity:
        # Both approaches fundamentally do the same amount of work - they generate all 2^n possible combinations, and for each combination, they perform O(m) operations to construct the result string.


# @lc code=end


#
# @lcpr case=start
# "a1b2"\n
# @lcpr case=end

# @lcpr case=start
# "3z4"\n
# @lcpr case=end

#
