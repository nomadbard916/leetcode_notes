#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from collections import defaultdict
from typing import Dict, List, Tuple


class TimeMap:
    def __init__(self):
        # each key maps to a list of ( timestamp, value )
        self.data: Dict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

        # O(1)

    def get(self, key: str, timestamp: int) -> str:
        # List[[timestamp, value]]
        data_pairs = self.data[key]
        if not data_pairs:
            return ""

        left, right = 0, len(data_pairs) - 1

        result = ""

        # essentially searching right-most for the largest ts less than target,
        # so bisect_right may be used,
        # but memory explodes when manually making timestamps list
        while left <= right:
            mid = (left + right) // 2

            mid_data_ts, mid_data_val = data_pairs[mid]

            if mid_data_ts <= timestamp:
                # This timestamp is valid, save the value
                result = mid_data_val
                # Look for a potentially larger valid timestamp
                left = mid + 1
            else:
                # This timestamp is too large, search left half
                right = mid - 1

        return result
        # O(log n)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
