#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
from bisect import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self):
        # need to get value by key => dict
        # while search by value, timestamp pair
        # => two lists to store value and timestamp for the same key in dict
        self._t = defaultdict(list)
        self._v = defaultdict(list)
        # * self._max_t helps to return early when timestamp already exceeds the max,
        # but not necessary
        # self._max_t = defaultdict(int)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._t[key].append(timestamp)
        self._v[key].append(value)
        # self._max_t[key] = max(self._max_t[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._t:
            return ""

        # if timestamp >= self._max_t[key]:
        #     return self._v[key][-1]

        if timestamp := bisect(self._t[key], timestamp):
            real_index = timestamp - 1
            return self._v[key][real_index]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
