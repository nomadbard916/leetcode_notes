#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # traverse through each node on decision tree,
        # then choose from option list, starting from nums.index(node) +1 to end of nums
        # record path and update option list in the process

        ans = []
        length = len(nums)

        # traverse with path and option list
        # index (when combined with len(nums)) can represent option list
        def traverse(current_path: list = [], starting_index: int = 0):
            # ending condition:
            # when index reaches out of bottom of decision tree
            if starting_index > length:
                return

            ans.append(current_path)

            for i in range(starting_index, length):
                current_num = nums[i]

                # update path list after current_num is traversed
                updated_path = current_path + [current_num]

                # manually going to the next index, ie. next level of decision tree
                traverse(updated_path, i + 1)

        traverse()

        return ans


# @lc code=end

