from collections import deque
from typing import List

nums: List[int] = [1, 2, 3]

# Monotonic Stack Pattern:
stack = []
for i in range(len(nums)):
    # Only remove from TOP (back)
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()  # Process element that found answer
        # Do something with idx

    stack.append(i)

k = 3
# Monotonic Deque Pattern:
dq = deque()
for i in range(len(nums)):
    # Remove from FRONT: elements outside window
    while dq and dq[0] < i - k + 1:
        dq.popleft()  # ← KEY DIFFERENCE!

    # Remove from BACK: maintain monotonic property
    while dq and nums[dq[-1]] < nums[i]:
        dq.pop()

    dq.append(i)
