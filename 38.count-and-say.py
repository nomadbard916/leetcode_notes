#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        def cal(s):
            count = 1
            length = len(s)
            ans = ""

            for i, c in enumerate(s):
                if i + 1 < length and s[i] != s[i + 1]:
                    ans = ans + str(count) + c
                    count = 1
                elif i + 1 < length:
                    count += 1

            ans = ans + str(count) + s[length - 1]

            return ans

        s = "1"
        for _ in range(1, n):
            s = cal(s)

        return s


# @lc code=end

