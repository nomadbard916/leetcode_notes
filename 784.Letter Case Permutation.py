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
        # ! sol1: backtracking
        result = []

        def backtrack(index: int, curr_path: List[str]):
            # * ending condition: if we've processed all characters
            if index == len(s):
                result.append("".join(curr_path))
                return

            curr_char = s[index]

            # * make decision, backtrack and cancel decision for each condition: lower alpha, upper alpha and digits.
            # for letters, try both lowercase and uppercase
            if curr_char.isalpha():
                #  try lowercase version
                curr_path.append(curr_char.lower())
                backtrack(index + 1, curr_path)
                curr_path.pop()

                # try uppercase version
                curr_path.append(curr_char.upper())
                backtrack(index + 1, curr_path)
                curr_path.pop()

            # for digits, keep as is
            else:
                curr_path.append(curr_char)
                backtrack(index + 1, curr_path)
                curr_path.pop()

        backtrack(0, [])
        return result

        # ! sol2: iterative with bit manipulation
        """
        Iterative solution using bit manipulation to generate all permutations.

        Example walkthrough with s = "a1B":
        - Letters at positions: [0, 2] (a and B)
        - num_letters = 2, so we need 2^2 = 4 permutations
        - Masks: 00, 01, 10, 11 (binary) = 0, 1, 2, 3 (decimal)

        Mask interpretation:
        - Bit 0 controls letter at position 0 (a)
        - Bit 1 controls letter at position 2 (B)
        - 0 = lowercase, 1 = uppercase
        """
        # * Step 1: Find all letter positions
        letter_positions = []
        for i, char in enumerate(s):
            if char.isalpha():
                letter_positions.append(i)

        # * Step 2: Calculate total permutations = 2^(number of letters)
        num_letters = len(letter_positions)
        total_permutations = 1 << num_letters  # 2 ^ num_letters

        result = []

        # * Step 3: Generate all possible bitmasks from 0 to 2^num_letters - 1
        for mask in range(total_permutations):
            # convert string to list for easier manipulation
            current = list(s)

            # * Step 4: Apply the mask to determine case for each letter
            for i, pos in enumerate(letter_positions):
                # Check if bit i is set in the current mask
                if mask & (1 << i):  # Bitwise AND with 2^i
                    current[pos] = current[pos].upper()
                else:
                    current[pos] = current[pos].lower()
            result.append("".join(current))

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
