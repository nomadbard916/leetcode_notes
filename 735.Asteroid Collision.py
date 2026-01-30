#
# @lc app=leetcode id=735 lang=python3
# @lcpr version=30305
#
# [735] Asteroid Collision
#

# @lc code=start
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
        tmp_stack = []
        # no need to sanity check

        for i, a in enumerate(asteroids):
            if i == 0:
                tmp_stack.append(a)
                continue

            # start here
            prev_a = asteroids[i-1]
            if a * prev_a < 0:
                # start comparison
                # a smaller
                if a < prev_a:
                    # destroyed
                    continue
                # a bigger
                if a > prev_a:
                    tmp_stack.pop()
                    tmp_stack.append
                # equal
                elif a == prev_a:
                    tmp_stack.pop()
            else:
                tmp_stack.append(a)

        return tmp_stack


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

