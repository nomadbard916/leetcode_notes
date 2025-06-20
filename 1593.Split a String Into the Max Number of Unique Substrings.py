#
# @lc app=leetcode id=1593 lang=python3
# @lcpr version=30104
#
# [1593] Split a String Into the Max Number of Unique Substrings
#

# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start: int, used: set[str]) -> int:
            max_splits = 0
            # * ending condition: reaching the end of the string
            if start == len(s):
                return max_splits

            # try all possible substrings starting from start
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring not in used:
                    used.add(substring)

                    # * make the decision with option list and path bringing down to next recursion level
                    # current level + result from recursive remaining
                    current_splits = 1 + backtrack(end, used)

                    max_splits = max(max_splits, current_splits)

                    # * cancel after the decision is made
                    used.remove(substring)

            return max_splits

        return backtrack(0, set())

        # Time and Space Complexity
        # Time Complexity: O(2^n) where n is the length of the string
        # - In the worst case, we explore all possible ways to split the string
        # - Each position can either start a new substring or extend the current one
        # - This gives us exponential possibilities

        # Space Complexity: O(n)
        # - Recursion stack depth: O(n) in the worst case
        # - Used set: O(n) to store at most n substrings
        # - Each substring storage: O(n) total characters across all substrings


# @lc code=end


#
# @lcpr case=start
# "ababccc"\n
# @lcpr case=end

# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n
# @lcpr case=end

#
