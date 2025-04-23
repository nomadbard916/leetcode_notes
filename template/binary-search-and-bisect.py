import bisect


# [left, right]
def binarysearch(nums, target):
    l, r = 0, len(nums) - 1

    # both ends closed
    while l <= r:
        # other languages may have 'overflow', therefore mid needs to be 'left + (right - left) /2'
        mid = (l + r) // 2

        if nums[mid] == target:
            # usually need to consider sanity check before returning mid.
            return mid
            # if sanity check doesn't pass, it needs to move left or right here to do next check

        # "mid" point itself is already searched
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1  # when not found


# 寻找左侧边界的二分搜索, a most commonly seen solution
# [left, right)
def left_bound(nums: List[int], target: int) -> int:
    left = 0
    # 注意
    right = len(nums)

    # 注意
    # 为什么 while 中是 < 而不是 <=？
    # 答：用相同的方法分析，因为 right = nums.length 而不是 nums.length - 1。
    # 因此每次循环的「搜索区间」是 [left, right) 左闭右开。
    # while(left < right) 终止的条件是 left == right，
    # 此时搜索区间 [left, left) 为空，所以可以正确终止。
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        # 为什么 left = mid + 1，right = mid ？和之前的算法不一样？

        # 答：这个很好解释，因为我们的「搜索区间」是 [left, right) 左闭右开，
        # 所以当 nums[mid] 被检测之后，下一步应该去 mid 的左侧或者右侧区间搜索，
        # 即 [left, mid) 或 [mid + 1, right)。

        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            # 注意
            right = mid

    return left
    # 如果 target 不存在，搜索左侧边界的二分搜索返回的索引是大于 target 的最小索引。

    # 如果想让 target 不存在时返回 -1 其实很简单，
    # 在返回的时候额外判断一下 nums[left] 是否等于 target 就行了，如果不等于，就说明 target 不存在。
    # 需要注意的是，访问数组索引之前要保证索引不越界。 如果索引越界，说明数组中无目标元素，返回 -1


# [left, right]
def left_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # 搜索区间为 [left, right]

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif nums[mid] > target:
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif nums[mid] == target:
            # 收缩右侧边界
            right = mid - 1

    # 判断 target 是否存在于 nums 中
    # 如果越界，target 肯定不存在，返回 -1
    if left < 0 or left >= len(nums):
        return -1

    # 判断一下 nums[left] 是不是 target
    return left if nums[left] == target else -1


# 寻找右侧边界的二分查找, a most commonly seen solution
# [left, right)
def right_bound(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        # 为什么这个算法能够找到右侧边界？
        # 当 nums[mid] == target 时，不要立即返回，而是增大「搜索区间」的左边界 left，
        # 使得区间不断向右靠拢，达到锁定右侧边界的目的。
        if nums[mid] == target:
            # 注意
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    # 注意
    # 为什么最后返回 left - 1 而不像左侧边界的函数，返回 left？
    # 而且我觉得这里既然是搜索右侧边界，应该返回 right 才对。

    # 答：首先，while 循环的终止条件是 left == right，
    # 所以 left 和 right 是一样的，你非要体现右侧的特点，
    # 返回 right - 1 好了。

    # 至于为什么要减一，这是搜索右侧边界的一个特殊点，
    # 关键在锁定右边界时的这个条件判断：
    # 因为我们对 left 的更新必须是 left = mid + 1，就是说 while 循环结束时，
    # nums[left] 一定不等于 target 了，而 nums[left-1] 可能是 target。
    # 至于为什么 left 的更新必须是 left = mid + 1，
    # 当然是为了把 nums[mid] 排除出搜索区间，这里就不再赘述。
    return left - 1
    # 如果你想在 target 不存在时返回 -1，很简单，
    # 只要在最后判断一下 nums[left-1] 是不是 target 就行了


# [left, right]
def right_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 这里改成收缩左侧边界即可
            left = mid + 1
    # 最后改成返回 left - 1
    if left - 1 < 0 or left - 1 >= len(nums):
        return -1
    return left - 1 if nums[left - 1] == target else -1
    # 由于 while 的结束条件为 right == left - 1，
    # 所以你把上述代码中的 left - 1 都改成 right 也没有问题，这样可能更有利于看出来这是在「搜索右侧边界」
    # return right if nums[right] == target else -1


# ! the ultimate comparison, all with [left, right]
def binary_search(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 找到目标值
            return mid
    # 没有找到目标值
    return -1


def left_bound(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 存在目标值，缩小右边界
            right = mid - 1
    # 判断是否存在目标值
    if left < 0 or left >= len(nums):
        return -1
    # 判断找到的左边界是否是目标值
    return left if nums[left] == target else -1


def right_bound(nums: List[int], target: int) -> int:
    # 设置左右下标
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            # 存在目标值，缩小左边界
            left = mid + 1
    # 判断是否存在目标值
    if right < 0 or right >= len(nums):
        return -1
    # 判断找到的右边界是否是目标值
    return right if nums[right] == target else -1


# from lucifer: 在实际的写代码过程中，我不会使用寻找满足条件的值模板，而是直接使用最左或者最右插入模板。
# 为什么呢？因为后者包含了前者，并还有前者实现不了的功能。比如我要实现寻找满足条件的值，
# 就可直接使用最左插入模板找到插入索引 i，只不过最后判断一下 nums[i] 是否等于 target 即可，
# 如果不等于则返回 -1，否则返回 i。这也是为什么我将二分分为两种类型，而不是为两种类型，而不是三種甚至四種的原因。


def bisect_left(A, x):
    # 内置 api, has very simple and elegant C implementation
    bisect.bisect_left(A, x)
    # 手写
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] >= x:
            r = mid - 1
        else:
            l = mid + 1
    return l


def bisect_right(A, x):
    # 内置 api, has very simple and elegant C implementation
    bisect.bisect_right(A, x)
    # 手写
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
    return l  # 或者 r + 1
