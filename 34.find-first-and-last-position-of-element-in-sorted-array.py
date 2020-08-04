#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        length = len(nums)

        def find_first() -> int:
            l, r = 0, length - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if (
                        # check if its left is not the target
                        # but mid -1 must be >= 0 to be in range
                        (mid - 1 >= 0 and nums[mid - 1] != target)
                        # the exception is when mid == 0, and it's naturally the leftmost one
                        or mid == 0
                    ):
                        return mid

                    # as the found one is not the first one, searching needs to continue
                    r = mid - 1

                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1

            return -1

        def find_last() -> int:
            l, r = 0, length - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    if (
                        # check if its right is not the target
                        # but mid +1 must not exceed length
                        (mid + 1 < length and nums[mid + 1] != target)
                        # the exception is when mid == length -1, and it's naturally the leftmost one
                        or mid == length - 1
                    ):
                        return mid
                    # as the found one is the first one, searching needs to continue
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1

            return -1

        # the first satisfying element
        first = find_first()
        # as last one is the first unsatisfying element
        last = find_last()

        return [first, last]

        # solution 2:
        # if target not in nums:
        #     return [-1, -1]

        # first = nums.index(target)

        # last = len(nums) - 1 - nums[::-1].index(target)

        # return [first, last]


# @lc code=end

