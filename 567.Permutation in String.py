#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30104
#
# [567] Permutation in String
#

# @lc code=start


import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # * sliding window => two pointer
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        # fill in container first
        for c in s1:
            need[c] += 1

        l, r = 0, 0
        valid_chars_cnt = 0

        while r < len(s2):
            # * step 1: keep enlarging the window until required chars count met
            curr_c_r = s2[r]
            # data manipulation in window
            if curr_c_r in need:
                window[curr_c_r] += 1
                if window[curr_c_r] == need[curr_c_r]:
                    valid_chars_cnt += 1
            r += 1

            # * step 2: check if to shrink left window side
            # the window is actually a fixed length one,
            # so we may change the "while" structure to "if"
            while r - l >= len(s1):
                # determine if valid substring is found
                if valid_chars_cnt == len(need):
                    return True
                curr_c_l = s2[l]
                # update data in window
                if curr_c_l in need:
                    if window[curr_c_l] == need[curr_c_l]:
                        valid_chars_cnt -= 1
                    window[curr_c_l] -= 1
                l += 1
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
