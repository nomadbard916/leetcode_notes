#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        if len(s) > 12:
            return ans

        def DFS(current_path: List[str] = [], option_list: str = s):
            # ending condition: iterated through the whole string
            # and successfully divided it to 4 groups as valid IP
            if len(option_list) == 0 and len(current_path) == 4:
                ans.append(".".join(current_path))
                return

            for i in range(1, 4):
                if len(option_list) < i:
                    continue

                current_num = option_list[:i]

                # consider current_num starting with 0 (except for 0 itself) to be illegal
                if str(int(current_num)) == current_num and int(current_num) <= 255:
                    updated_path = current_path + [current_num]
                    updated_options = option_list[i:]

                    DFS(updated_path, updated_options)

        DFS()

        return ans


# @lc code=end

