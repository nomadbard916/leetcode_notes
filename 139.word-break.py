#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # ! DRAFT
        s_length = len(s)

        # sanity check
        if s_length < len(min(wordDict, key=len)):
            return False

        def backtrack(current_path="", option_list=wordDict):
            if current_path == s:
                return True

            # ending condition: out of bound
            if len(current_path) > s_length:
                return

            for word in option_list:
                backtrack(current_path + word, option_list)

            return False


# @lc code=end

