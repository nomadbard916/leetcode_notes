#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30104
#
# [567] Permutation in String
#

# @lc code=start


from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # * sliding window => two pointer
        needed = defaultdict(int)
        window = defaultdict(int)
        # fill in container first
        for c in s1:
            needed[c] += 1

        l, r = 0, 0
        valid_chars_cnt = 0

        while r < len(s2):
            # * step 1: keep enlarging the window until required chars count met
            curr_c_r = s2[r]
            # data manipulation in window
            if curr_c_r in needed:
                window[curr_c_r] += 1
                if window[curr_c_r] == needed[curr_c_r]:
                    valid_chars_cnt += 1
            r += 1

            # * step 2: check if to shrink left window side
            # In this problem, you are looking for a substring in s2 that is a permutation of s1.
            # Since a permutation must have the same length as s1,
            # the sliding window should always be of length len(s1) as it moves through s2.
            # That's why the code checks if r - l >= len(s1):—to ensure the window size matches s1's length before checking for a valid permutation.

            # the window length is actually fixed to s1,
            # window too big, should shrink
            while r - l + 1 > len(s1):
                # determine if valid substring is found
                if valid_chars_cnt == len(needed):
                    return True
                curr_c_l = s2[l]
                # update data in window
                if curr_c_l in needed:
                    if window[curr_c_l] == needed[curr_c_l]:
                        valid_chars_cnt -= 1
                    window[curr_c_l] -= 1
                l += 1
        return False

        # ! sol2: it's not folowing the template, but easier to understand    if len(s1) > len(s2):

        from collections import Counter
        from typing import Dict

        # Count frequency of characters in s1
        s1_count: Dict[str, int] = Counter(s1)
        window_size = len(s1)

        # Initialize sliding window with first window_size characters of s2
        window_count: Dict[str, int] = Counter(s2[:window_size])

        # Check if first window matches
        if window_count == s1_count:
            return True

        # Slide the window through the rest of s2
        for i in range(window_size, len(s2)):
            # Add the new character (right side of window)
            new_char = s2[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            # Remove the old character (left side of window)
            old_char = s2[i - window_size]
            window_count[old_char] -= 1

            # Remove the character from counter if count becomes 0
            # This keeps the counter clean and helps with comparison
            if window_count[old_char] == 0:
                del window_count[old_char]

            # Check if current window matches s1's character frequency
            if window_count == s1_count:
                return True

        return False


# @lc code=end


#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#
