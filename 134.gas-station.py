#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #  many say it's "greedy" algorithm
        # maybe ref. to '121. Best time to buy and sell stock'

        n = len(gas)

        # initialize
        fuel_level, start_index, total_gas = 0, 0, 0

        for i in range(n):
            # this one essentially considers availability as:
            # ......sum  of diffs >= 0, especially when it's circular
            net_gas = gas[i] - cost[i]

            # collect gas and record total
            total_gas += net_gas
            fuel_level += net_gas

            # think negatively first:
            # if a stop cannot be the starting one,
            # go to next one, set it as start, and zero current_gas
            if fuel_level < 0:
                start_index = i + 1
                fuel_level = 0

        return -1 if total_gas < 0 else start_index


# @lc code=end
