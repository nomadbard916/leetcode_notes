#
# @lc app=leetcode id=528 lang=python3
# @lcpr version=30305
#
# [528] Random Pick with Weight
#

# @lc code=start

import bisect
import random
from typing import List


class Solution:
    #     Key insights
    # - The dart-on-a-number-line metaphor: Imagine laying the indices end-to-end on a number line,
    # each occupying a segment proportional to its weight.
    # A uniform random dart thrown at the line lands in index i's segment with exactly the right probability.
    # Prefix sums build that number line; binary search identifies which segment the dart hit.
    # - bisect_left vs bisect_right: We use bisect_left on prefix sums. With random() * total (exclusive of total),
    # if the dart hits exactly on a boundary it should go into the right bucket (the one that starts there),
    # which is what bisect_left does — it returns the leftmost position where we could insert,
    # i.e., it never skips past an exact match.

    def __init__(self, w: List[int]):
        """
        Build the prefix-sum array once.

        Example: w = [1, 3, 2]
          prefix_sums = [1, 4, 6]
          Index 0 owns dart range [0, 1)   — probability 1/6
          Index 1 owns dart range [1, 4)   — probability 3/6
          Index 2 owns dart range [4, 6)   — probability 2/6
        """
        self.prefix_sum: List[int] = []
        running = 0
        for weight in w:
            running += weight
            self.prefix_sum.append(running)
        # running == total weight after the loop
        self.total = running

    def pickIndex(self) -> int:
        """
        Throw a dart uniformly in [0, total) and binary-search which bucket
        it lands in.

        random.random() ∈ [0.0, 1.0)  →  * total  →  [0.0, total)

        bisect_left(a, x) returns the leftmost position i such that a[i] >= x.
        That is the index whose prefix-sum boundary is first >= our dart value,
        meaning the dart landed inside that bucket.
        """
        dart = random.random() * self.total
        return bisect.bisect_left(self.prefix_sum, dart)

    #     Complexity
    # Operation,Time Complexity,Space Complexity
    # __init__,O(n) — One pass to build prefix sums,O(n)
    # pickIndex,O(logn) — Binary search,O(1) extra


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end


#
# @lcpr case=start
# ["Solution","pickIndex"]\n[[[1]],[]]\n["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]\n[[[1,3]],[],[],[],[],[]]\n
# @lcpr case=end

#
