import bisect

# from lucifer: 在实际的写代码过程中，我不会使用寻找满足条件的值模板，而是直接使用最左或者最右插入模板。
# 为什么呢？因为后者包含了前者，并还有前者实现不了的功能。比如我要实现寻找满足条件的值，
# 就可直接使用最左插入模板找到插入索引 i，只不过最后判断一下 nums[i] 是否等于 target 即可，
# 如果不等于则返回 -1，否则返回 i。这也是为什么我将二分分为两种类型，而不是为两种类型，而不是三種甚至四種的原因。


def bisect_left(A, x):
    # 内置 api
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
    # 内置 api
    bisect.bisect_right(A, x)
    # 手写
    l, r = 0, len(A) - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
    return l # 或者 r + 1
