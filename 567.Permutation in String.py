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
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in s1:
            need[c] += 1

        left, right, valid = 0, 0, 0

        while right < len(s2):
            c = s2[right]
            right += 1
            # data manipulation in window
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # check if to shrink left side of window
            while right - left >= len(s1):
                # determine if valid substring is found
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
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
