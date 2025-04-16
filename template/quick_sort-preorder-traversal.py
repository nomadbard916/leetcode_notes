def sort(nums: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    # ****** 前序位置 ******
    # 对 nums[lo..hi] 进行切分，将 nums[p] 排好序
    # 使得 nums[lo..p-1] <= nums[p] < nums[p+1..hi]
    p = partition(nums, lo, hi)

    # 去左右子数组进行切分
    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)
