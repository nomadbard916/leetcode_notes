from collections import deque

#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        # deal with order
        # deal with unordered record

        # main container to make lookup as fast as possible with O(1),
        # yet it's unordered, needs another container to record orders
        self.m = {}
        # make add/delete as fast as possible with O(1) with deque
        self.q = deque()

        self.c = capacity

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        self.q.remove(key)
        self.q.append(key)

        value = self.m[key]

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.q.remove(key)
        else:
            if len(self.q) == self.c:
                oldest = self.q.popleft()
                del self.m[oldest]

        self.q.append(key)
        self.m[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

