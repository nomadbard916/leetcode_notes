#
# @lc app=leetcode id=395 lang=python3
# @lcpr version=30104
#
# [395] Longest Substring with At Least K Repeating Characters
#

# @lc code=start
from collections import defaultdict


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
        LEN = len(s)
        if not s or k > LEN:
            return 0
        if k == 1:  # If k is 1, every character satisfies the condition
            return LEN

        max_unique_chars = len(set(s))

        result = 0

        # Try each possible count of unique characters
        # If we allow any number of unique characters in our window,
        # we can't ensure each unique character appears ≥ k times
        # We need precise control over exactly how many unique characters are in our current window
        for unique_char_cnt_target in range(1, max_unique_chars + 1):
            # Initialize sliding window
            start = 0
            char_counts = defaultdict(int)
            curr_unique_char_count = 0  # Number of unique chars in current window
            at_least_k_count = 0  # Number of chars appearing at least k times

            # ! Expand window in caterpillar form
            for end in range(LEN):
                # * handle end char
                # Add the right character to our window
                if char_counts[s[end]] == 0:
                    curr_unique_char_count += 1
                char_counts[s[end]] += 1

                # Update count of chars appearing at least k times
                if char_counts[s[end]] == k:
                    at_least_k_count += 1

                # ! shrink window while we have too many unique chars
                while curr_unique_char_count > unique_char_cnt_target:
                    # * Remove the left character from our window
                    # Because we're about to remove one occurrence of this character, it will no longer meet the k-requirement
                    if char_counts[s[start]] == k:
                        at_least_k_count -= 1

                    char_counts[s[start]] -= 1
                    # If after decreasing, the character count becomes 0
                    # We decrease the count of unique characters in our current window
                    # Because this character no longer appears in our window at all
                    if char_counts[s[start]] == 0:
                        curr_unique_char_count -= 1

                    # let left character step right
                    start += 1

                # ! Check if all chars in the window appear at least k times
                if curr_unique_char_count == at_least_k_count:
                    result = max(result, end - start + 1)

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
