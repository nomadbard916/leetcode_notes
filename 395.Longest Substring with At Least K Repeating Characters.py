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
        # # it's already O(n) here
        # cnt = collections.Counter(s)
        # # starting position of the current segment we are considering
        # st = 0
        # # max substring length found so far
        # maxst = 0
        # for i, c in enumerate(s):
        #     # an character that appears fewer than k times int hte entire string
        #     # cannot be part of a valid answer.
        #     # These characters must be excluded entirely from any valid substring.
        #     if cnt[c] < k:
        #         # when the segment is broken due to char less than k which will be "divider",
        #         # start checking recursively the previous segment in [st, i) to determine maxst
        #         maxst = max(maxst, self.longestSubstring(s[st:i], k))
        #         # move the pointer to next possible segment start after this invalid character
        #         st = i + 1
        #
        # # maxst is determined as "length of segment" in previously passed in [st:i) if st is 0 i.e as a whole until divider char
        #
        # # there's still need to check the last segment,
        # # as the focus was on "invlid" characters
        # # while there are remaining segment not checked yet
        # # in the final loop for valid segment, the answer is exactly as the string length
        # return len(s) if st == 0 else max(maxst, self.longestSubstring(s[st:], k))

        # The idea is that any characters in the string that do not satisfy the requirement break the string in multiple parts that do not contain these characters, and for each part we should check the requirement again. There are similar solutions (not many), though most use string methods like split or count, which keep some important details hidden. Here I am also using Counter for short code but it’s just replacing a usual dictionary and a single obvious loop to calculate counts of letters.

        # Concerning complexity, it is indeed formally O(N), like it was mentioned in another solution despite recursion, because at each level of recursion we look at maximum 2N characters, and there can be not more than 26 levels of recursion, because we remove at least one character from 26 possible characters each time we move to the next level.

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
