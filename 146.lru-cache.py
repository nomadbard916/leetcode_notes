from collections import deque
from typing import Dict

#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#


# @lc code=start
class LRUCache:
    # deal with order
    # deal with unordered record

    def __init__(self, capacity: int):
        # main container to make lookup as fast as possible with O(1),
        # it's ordered already after py 3.7, but still lacks some convenient helpers in OrderedDict
        self.cache: Dict[int, int] = {}

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # move to end: pop and re-add
        value = self.cache.pop(key)
        self.cache[key] = value
        # OrderedDict has a very convenient move_to_end(key)

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove from old position first
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # remove oldest item first
            oldest = next(iter(self.cache))
            del self.cache[oldest]
            # OrderedDict has a very convenient popitem(last=False)

        # add to end
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
