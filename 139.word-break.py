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

        DPtable: dict = {}

        # sanity check
        if s_length == 0 or len(wordDict) == 0:
            return False

        def backtrack(option_list=s):
            option_length = len(option_list)

            if option_list in DPtable:
                return DPtable[option_list]

            if option_list in wordDict:
                DPtable[option_list] = True
                return True

            for i in range(0, option_length):
                checking = option_list[:i]
                checkable = option_list[i:]

                if checkable in wordDict and backtrack(checking):
                    DPtable[option_list] = True
                    return True

            DPtable[option_list] = False
            return False

        return backtrack()


# @lc code=end

