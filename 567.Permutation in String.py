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
            c = s2[r]
            # data manipulation in window
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid_chars_cnt += 1
            r += 1

            # check if to shrink left side of window
            while r - l >= len(s1):
                # determine if valid substring is found
                if valid_chars_cnt == len(need):
                    return True
                d = s2[l]
                # update data in window
                if d in need:
                    if window[d] == need[d]:
                        valid_chars_cnt -= 1
                    window[d] -= 1
                l += 1
        # substring not found
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
