#
# @lc app=leetcode id=735 lang=python3
# @lcpr version=30305
#
# [735] Asteroid Collision
#

# @lc code=start
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Main solution using stack to simulate collisions.

        Core logic:
        - Right-moving (+) asteroids go to stack (potential collision targets)
        - Left-moving (-) asteroids collide with stack top if top is positive
        - Same direction asteroids never collide

        Time: O(n) - each asteroid pushed/popped at most once
        Space: O(n) - stack storage
        """
        """
        * nouns and verbs:
        intergers in a row, indices... position, array, absolute value: size, sign: direction, same speed, state, explode: smaller one, both when same size , never meet: same direction

        * pattern kws
        in a row

        * structural kws
        no? asteroids[i] != 0
        absolute values (sizes)
        directions: positive = right, negative = left; no two same position start

        * algo concepts:
        collision: need to track interactions
        final state after all collisions: process until stable
        destroy based on size: comparison
        order matters: sequential processing
        in a row => stack

        * mental categories:
        stack: for tracking right-moving asteroids
        state machine: stable vs collision states

        * tricky kws:
        moving in sae direction: no collision
        equal size: both destroyed
        explosion rules: remove from result

        * pattern kws:
        ?
        """
        # * sol1
        stack: List[int] = []
        # no need to sanity check from problem requirement

        for asteroid in asteroids:
            """
            📊 Complete State Transition Table
            ┌─────────────┬──────────────┬─────────────┬──────────────────────┬─────────┐
            │ Stack State │ Stack Top    │ Current (a) │ Action               │ alive   │
            ├─────────────┼──────────────┼─────────────┼──────────────────────┼─────────┤
            │ Empty       │ N/A          │ > 0         │ Add a                │ True    │
            │ Empty       │ N/A          │ < 0         │ Add a                │ True    │
            ├─────────────┼──────────────┼─────────────┼──────────────────────┼─────────┤
            │ Not Empty   │ > 0 (right→) │ > 0 (right→)│ Add a (no collision) │ True    │
            │ Not Empty   │ > 0 (right→) │ < 0 (left←) │ COLLISION! Enter loop│ Depends │
            │ Not Empty   │ < 0 (left←)  │ > 0 (right→)│ Add a (no collision) │ True    │
            │ Not Empty   │ < 0 (left←)  │ < 0 (left←) │ Add a (no collision) │ True    │
            └─────────────┴──────────────┴─────────────┴──────────────────────┴─────────┘
            """
            # Positive asteroid: assume it's the normality,
            # and just add to the tracking stack
            if asteroid > 0:
                stack.append(asteroid)
                continue

            # Negative asteroid - potential collision zone
            # Keep colliding  by popping the stack,while:
            while (
                # 1. Stack has asteroids
                stack
                and
                # 2. Stack top is moving right (positive)
                stack[-1] > 0
                and
                # 3. Stack top is smaller than current (in absolute value)
                stack[-1] < abs(asteroid)
            ):
                stack.pop()

            # After collision loop, check final state to handle cases that the loop never entered
            # Case 1: Equal size collision - both destroyed
            if stack and stack[-1] == abs(asteroid):
                stack.pop()
            # Case 2: Stack empty OR stack top is also moving left
            # No collision possible, add current asteroid
            elif not stack or stack[-1] < 0:
                stack.append(asteroid)
            # Case 3: Stack top is larger positive (current destroyed)
            # Do nothing - current asteroid is destroyed
            else:
                continue

        return stack

        # * sol2: using state tracker
        stack = []
        # no need to sanity check

        for a in asteroids:
            alive = True
            while alive and stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] > -a:
                    alive = False
                # both destroy
                else:
                    stack.pop()
                    alive = False
            if alive:
                stack.append(a)
        return stack

        # Complexity Analysis
        # - Time Complexity: O(n)
        # Each asteroid enters stack exactly once
        # Each asteroid leaves stack at most once
        # Total operations = 2n max → O(n)

        # - Space Complexity: O(n)
        # Stack can hold all asteroids in worst case (e.g., all positive: [1,2,3,4,5])


# @lc code=end


#
# @lcpr case=start
# [5,10,-5]\n
# @lcpr case=end

# @lcpr case=start
# [8,-8]\n
# @lcpr case=end

# @lcpr case=start
# [10,2,-5]\n
# @lcpr case=end

# @lcpr case=start
# [3,5,-6,2,-1,4]\n
# @lcpr case=end

#
