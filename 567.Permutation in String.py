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
        valid = 0

        while r < len(s2):
            c = s2[r]
            r += 1
            # data manipulation in window
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # check if to shrink left side of window
            while r - l >= len(s1):
                # determine if valid substring is found
                if valid == len(need):
                    return True
                d = s2[l]
                l += 1
                # update data in window
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
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
