#
# @lc app=leetcode id=395 lang=python3
# @lcpr version=30104
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # sol 1: divide and conquer

        # sol 2: two pointers
        if not s or k > len(s):
            return 0

        # Edge case: if k is 1, every character satisfies the condition
        if k == 1:
            return len(s)

        result = 0

        # The key insight is to try all possible number of unique characters
        # Maximum number of unique characters in s
        max_unique = len(set(s))

        for num_unique_target in range(1, max_unique + 1):
            # Reset counters for each target number of unique characters
            char_count = {}
            start = 0
            end = 0
            unique_count = 0  # Count of unique characters in current window
            valid_count = 0  # Count of characters that appear at least k times

            while end < len(s):
                # Expand the window by including the right character
                if s[end] not in char_count:
                    char_count[s[end]] = 0
                    unique_count += 1

                char_count[s[end]] += 1

                # If this character now appears k times, increment valid_count
                if char_count[s[end]] == k:
                    valid_count += 1

                # Shrink the window when we have more unique characters than our target
                while unique_count > num_unique_target:
                    # Reduce count of character at start of window
                    char_count[s[start]] -= 1

                    # If this character appeared exactly k times before, decrement valid_count
                    if char_count[s[start]] == k - 1:
                        valid_count -= 1

                    # If this character no longer exists in our window
                    if char_count[s[start]] == 0:
                        del char_count[s[start]]
                        unique_count -= 1

                    start += 1

                # If all characters in current window appear at least k times
                if unique_count == valid_count:
                    result = max(result, end - start + 1)

                end += 1

        return result


# @lc code=end


#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#
