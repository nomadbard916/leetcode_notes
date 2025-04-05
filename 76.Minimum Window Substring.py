#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=30104
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left, right, valid = 0, 0, 0

        # record the starting index and length of
        # min covering substring
        start = 0
        length = float("inf")
        while right < len(s):
            # char-moving into window
            c = s[right]
            # enlarge the window
            right += 1
            # update data within window
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # check if to shrink left window side
            while valid == len(need):
                # update min covering substring
                if right - left < length:
                    start = left
                    length = right - left
                # char moving out of window
                d = s[left]
                # shrink the window
                left += 1
                # update data in window
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # return min covering substring
        return "" if length == float("inf") else s[start : start + length]


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
