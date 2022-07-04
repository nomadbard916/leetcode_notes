#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import Counter, List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window
        ans = []
        LEN_P, LEN_S = len(p), len(s)

        if LEN_P > LEN_S:
            return ans

        # init counters, with s start from 'before' the first position p fully fits in
        # trick: update k, v in counter_s with sliding window
        # to avoid duplicated counter init
        counter_p, counter_s = Counter(p), Counter(s[: LEN_P - 1])

        for idx_r in range(LEN_P - 1, LEN_S):
            # let right step onto char first and include right as counted
            right_char_s = s[idx_r]
            counter_s[right_char_s] += 1

            # locate left by substracting from right
            idx_l = idx_r - LEN_P + 1
            if counter_s == counter_p:
                ans.append(idx_l)

            # exclude left from window to prepare for next iteration
            left_char_s = s[idx_l]
            counter_s[left_char_s] -= 1

            # remove counter item to avoid different counter contents
            if counter_s[left_char_s] == 0:
                del counter_s[left_char_s]

        return ans

        # sol2: two-pointer, but not as clean as sol1
        # count = collections.Counter()
        # M, N = len(s), len(p)
        # left, right = 0, 0
        # pcount = collections.Counter(p)
        # res = []
        # while right < M:
        #     count[s[right]] += 1
        #     if right - left + 1 == N:
        #         if count == pcount:
        #             res.append(left)
        #         count[s[left]] -= 1
        #         if count[s[left]] == 0:
        #             del count[s[left]]
        #         left += 1
        #     right += 1
        # return res


# @lc code=end
