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
        * nouns and verbs:
        intergers in a row, indices... position, array, absolute value: size, sign: direction, same speed, state, explode: smaller one, both when same size , never meet: same direction

        * pattern kws
        in a row

        * structural kws
        no? asteroids[i] != 0

        * algo concepts:
        in a row => stack

        * mental categories:
        ?

        * tricky kws:
        explosion rules

        * pattern kws:
        ?
        """
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
                else :
                    stack.pop()
                    alive= False
            if alive:
                stack.append(a)
        return stack




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
