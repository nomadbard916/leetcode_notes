#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # determine if this num belongs to Fibonacci sequence

        def DFS(current_path: List[int] = [], option_list: str = num) -> bool:
            # ending condition: not Fib
            if (
                len(current_path) >= 3
                and current_path[-1] != current_path[-2] + current_path[-3]
            ):
                return False

            # ending condition: iterated whole string and remaining are still Fib
            if len(option_list) == 0 and len(current_path) >= 3:
                return True

            for i, digit in enumerate(option_list):
                current_str = option_list[: i + 1]

                # eliminating 00
                if current_str[0] == "0" and len(current_str) != 1:
                    continue

                updated_path = current_path + [int(current_str)]
                updated_options = option_list[i + 1 :]

                if DFS(updated_path, updated_options):
                    return True

            return False

        return DFS()


# @lc code=end

