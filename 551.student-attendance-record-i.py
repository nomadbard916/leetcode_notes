from collections import Counter

#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0

        for record in s:
            if record == "A":
                A_count += 1

        if A_count > 1:
            return False

        if "LLL" in s:
            return False

        return True


# @lc code=end

