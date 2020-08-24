#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    # https://songhuiming.github.io/pages/2018/03/18/leetcode-139-word-break/
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #  slicing and checking string recursively and record the substring in "used" dict
        # return true when the whole string is done comparison
        s_length: int = len(s)

        memo: dict = {}

        # sanity check
        if s_length == 0 or len(wordDict) == 0:
            return False

        def backtrack(option_list=s):
            option_length = len(option_list)

            # ending condition: the ramaining string exist in wordDict
            if option_list in wordDict:
                memo[option_list] = True
                return True

            # ending condition: the ramaining string is already recorded to be breakable
            if option_list in memo:
                return memo[option_list]

            for i in range(0, option_length):
                # checking from the beginning, the recursively checking the remaining parts
                checking = option_list[:i]
                checkable = option_list[i:]

                # if a part is breakable, then the remaining part must also be breakable
                if checking in wordDict and backtrack(checkable):
                    memo[option_list] = True
                    return True

            memo[option_list] = False
            return False

        return backtrack()


# @lc code=end

