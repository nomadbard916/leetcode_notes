def binarysearch(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        # other languages may have 'overflow', therefore mid needs to be 'left + (right - left) /2'
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1  # when not found
