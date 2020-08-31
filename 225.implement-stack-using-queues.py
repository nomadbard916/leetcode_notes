from collections import deque

#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:
    # don't use native methods of deque
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

        # move all elements in front of x to after x
        elements_ahead = len(self.stack) - 1

        while elements_ahead > 0:
            current_first = self.stack.popleft()
            self.stack.append(current_first)
            elements_ahead -= 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        return self.stack.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """

        return self.stack[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """

        return bool(not len(self.stack))


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

