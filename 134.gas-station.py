#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #  many say it's "greedy" algorithm
        # maybe ref. to '121. Best time to buy and sell stock'

        # sanity check: total gas must be >= total cost
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)

        # initialize
        current_gas_stock, total_gas, start_index = 0, 0, 0

        # there must exist one unique answer or none
        for i in range(n):
            # this one essentially considers availability as:
            # ......sum  of diffs >= 0, especially when it's circular
            current_net_gas_diff = gas[i] - cost[i]

            # think negatively first:
            # if a stop cannot be the starting one, go to next one and set it start
            updated_gas_stock = current_gas_stock + current_net_gas_diff
            if updated_gas_stock < 0:
                start_index = i + 1
                current_gas_stock = 0
            else:
                current_gas_stock = updated_gas_stock

            # double check total gas won't be < 0 after iterated every stop
            total_gas = total_gas + current_net_gas_diff

        return start_index if total_gas >= 0 else -1


# @lc code=end

