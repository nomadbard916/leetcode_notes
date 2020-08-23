#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 解題思路：將羅馬數字轉換成對應的整數。首先將羅馬數字翻轉，從小的開始累加，如果遇到CM（MC=1000-100=900）這種該怎麼辦呢？因為翻轉過來是MC，M=1000先被累加，所以使用一個prev_val變量，把M記錄下來，如果下一個數小於M，那麼減兩次C，然後將C累加上 (CM = M -C = M - 2C + C)，這個實現比較巧妙簡潔。

        symbol_val = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        reversed_s = s[::-1]

        sum = 0

        prev_val = None

        for s in reversed_s:
            if prev_val and symbol_val[s] < prev_val:
                sum -= 2 * symbol_val[s]
            sum += symbol_val[s]
            prev_val = symbol_val[s]

        return sum


# @lc code=end

