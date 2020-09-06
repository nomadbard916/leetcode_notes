#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [letter for letter in S if letter.isalpha()]

        ans = []

        for char in S:
            if char.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(char)

        return "".join(ans)


# @lc code=end

