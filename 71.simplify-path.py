#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # back and forth with conditions => stack
        stack = []
        dirs = path.split("/")

        for dir in dirs:
            # consider '.' for current level and '//' that renders empty string after split
            if not dir or dir == ".":
                continue

            if dir == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return "/" + "/".join(stack)


# @lc code=end

