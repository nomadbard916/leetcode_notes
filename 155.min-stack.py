#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        current_min = self.getMin()
        if current_min is None or current_min > x:
            current_min = x

        # all the previous state of current_min are recorded,
        # no need to worry about ordering
        self.stack.append((x, current_min))

        # or you may make another min_stack to record min values

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
