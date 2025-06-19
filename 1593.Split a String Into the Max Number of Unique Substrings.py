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
            if start == len(s):
                return max_splits

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring not in used:
                    used.add(substring)

                    current_splits = 1 + backtrack(end, used)

                    max_splits = max(max_splits, current_splits)

                    used.remove(substring)

            return max_splits

        return backtrack(0, set())


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
