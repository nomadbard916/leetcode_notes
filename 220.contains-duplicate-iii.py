#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
from typing import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # limit1:
        # |j−i|<=k

        # limit2:
        # |nums[j]−nums[i]|<=t
        # ⟺ |nums[j]/t−nums[i]/t|<=1
        # ⟺ ⌊nums[j]/t⌋∈ {⌊nums[i]/t⌋−1,⌊nums[i]/t⌋,⌊nums[i]/t⌋+1}

        #  sanity check
        if k < 1 or t < 0:
            return False

        # OrderedDict is needed to popitem() with FIFO,
        # albeit dict after Python 3.7 is ordered FIFO by default
        dic = OrderedDict()

        for num in nums:
            key = num if t == 0 else num // t

            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(num - m) <= t:
                    return True

            # overdistanced, need to ignore previous items
            if len(dic) == k:
                dic.popitem(last=False)

            dic[key] = num

        return False


# @lc code=end

