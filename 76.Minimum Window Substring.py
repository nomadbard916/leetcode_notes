#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=30104
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # * sliding window => two pointer
        char_cnt_needed = {}
        char_cnt_window = {}

        # populate needed chars count mapping
        for c in t:
            char_cnt_needed[c] = char_cnt_needed.get(c, 0) + 1

        l, r = 0, 0
        valid_chars_cnt = 0

        # record the starting index and length of min covering substring
        res_start = 0
        res_length = float("inf")
        while r < len(s):
            # * step 1: keep enlarging the window until required chars count met
            # char-moving into window
            c = s[r]
            # update data within window
            if c in char_cnt_needed:
                char_cnt_window[c] = char_cnt_window.get(c, 0) + 1
                if char_cnt_window[c] == char_cnt_needed[c]:
                    valid_chars_cnt += 1
            # enlarge the window
            r += 1

            # * step 2: check if to shrink left window side
            while valid_chars_cnt == len(char_cnt_needed):
                # update min covering substring
                if r - l < res_length:
                    res_start = l
                    res_length = r - l
                # char moving out of window
                d = s[l]
                # update data in window
                if d in char_cnt_needed:
                    if char_cnt_window[d] == char_cnt_needed[d]:
                        valid_chars_cnt -= 1
                    char_cnt_window[d] -= 1
                # shrink the window
                l += 1

        if res_length == float("inf"):
            return ""

        # return min covering substring
        return s[res_start : res_start + res_length]


# @lc code=end


#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#
