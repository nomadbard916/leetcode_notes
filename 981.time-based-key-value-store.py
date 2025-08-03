#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict
from typing import Dict, List


class TimeMap:
    def __init__(self):
        # each key maps to a list of [timestamp, value]
        self.data: Dict[str, List[List]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        # List[[timestamp, value]]
        data_pairs = self.data[key]

        left, right = 0, len(data_pairs) - 1

        result = ""

        while left <= right:
            mid = (left + right) // 2

            mid_data_pair_ts, mid_data_pair_val = data_pairs[mid]

            if mid_data_pair_ts <= timestamp:
                # This timestamp is valid, save the value
                result = mid_data_pair_val
                # Look for a potentially larger valid timestamp
                left = mid + 1
            else:
                # This timestamp is too large, search left half
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
