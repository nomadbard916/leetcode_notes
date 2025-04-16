# 若要对 nums[lo..hi] 进行排序，我们先对 nums[lo..mid] 排序，
# 再对 nums[mid+1..hi] 排序，最后把这两个有序的子数组合并，整个数组就排好序了。

# 先对左右子数组排序，然后合并（类似合并有序链表的逻辑），你看这是不是二叉树的后序遍历框架？另外，这不就是传说中的分治算法嘛，不过如此呀。

# 定义：排序 nums[lo..hi]
def sort(nums: List[int], lo: int, hi: int) -> None:
    if lo == hi:
        return
    mid = (lo + hi) // 2
    # 利用定义，排序 nums[lo..mid]
    sort(nums, lo, mid)
    # 利用定义，排序 nums[mid+1..hi]
    sort(nums, mid + 1, hi)

    # ****** 后序位置 ******
    # 此时两部分子数组已经被排好序
    # 合并两个有序数组，使 nums[lo..hi] 有序
    merge(nums, lo, mid, hi)
