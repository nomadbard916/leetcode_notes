#
# @lc app=leetcode id=388 lang=python3
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # DFS or stack might work

        # define initial (depth which is out of range, current string length)
        stack = [(-1, 0)]
        max_len: int = 0

        # deal with each layer of folder separated by '\n'
        for node_name in input.split("\n"):
            current_depth: int = node_name.count("\t")
            # rewrite node_name to get rid of tab
            node_name: str = node_name.replace("\t", "")

            # check if current depth is less than or equal to latest stack item
            # as it's enough to leave only one folder in the same level
            while stack and current_depth <= stack[-1][0]:
                stack.pop()
            previous_path_length: int = stack[-1][1]

            # consider file, just update max lengths as it's what we want
            if "." in node_name:
                max_len: int = max(max_len, len(node_name) + previous_path_length)
            # consider path, put into stack as it implies next level
            # and no need to update length
            else:
                current_folder_info: tuple = (
                    current_depth,
                    # put / after folder name
                    len(node_name) + previous_path_length + 1,
                )

                stack.append(current_folder_info)

        return max_len


# @lc code=end

