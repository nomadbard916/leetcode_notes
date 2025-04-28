#
# @lc app=leetcode id=560 lang=python3
# @lcpr version=30104
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        First of all, the basic idea behind this code is that, whenever sums has increased by a value of k, we’ve found a subarray of sums=k. I’ll also explain why we need to initialise 0 in the hashmap. Example: Let’s say our elements are [1,2,1,3] and k = 3. and our corresponding running sums = [1,3,4,7] Now, if you notice the running sums array, from 1->4, there is increase of k and from 4->7, there is an increase of k. So, we’ve found 2 subarrays of sums=k.

        But, if you look at the original array, there are 3 subarrays of sums==k. Now, you’ll understand why 0 comes in the picture.

        In the above example, 4-1=k and 7-4=k. Hence, we concluded that there are 2 subarrays. However, if sums==k, it should’ve been 3-0=k. But 0 is not present in the array. To account for this case, we include the 0. Now the modified sums array will look like [0,1,3,4,7]. Now, try to see for the increase of k.
        """

        # first would would think of sliding window, But this fails for cases with negative numbers or zero, which the problem doesn't restrict.
        # That's why the prefix sum + hash map approach is actually the standard way to solve this problem, as it handles all cases including negative numbers and is still O(n).
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count

        # sol2: plain prefix sum
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  # Initialize with 0:1 for subarrays that start from index 0

        for num in nums:
            # Update the running sum
            prefix_sum += num

            # If (prefix_sum - k) exists in the hash map, it means we have subarrays that sum to k
            if prefix_sum - k in sum_count:
                count += sum_count[prefix_sum - k]

            # Update the prefix sum count in our hash map
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1

        return count


# @lc code=end


#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#
