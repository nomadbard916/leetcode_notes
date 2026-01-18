#
# @lc app=leetcode id=895 lang=python3
# @lcpr version=30305
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:
    """
    nouns and verbs:
    push...top of the stack, stack, pop... remove and return, most frequent element, construct

    pattern kws: no?

    structural kws:
    most frequent, val might be big int, calls may need to consider performance with 2* 10^4, remove and return, tie: closest to the stack's top

    map to algo:
    most frequent => counter?

    mental category: no?

    tricky kws: no?

    pattern kws: no?
    """

    # counter for each element? => ++ when push, -- when pop
    # what should I do when pop? find the first? it doesn't seem to care about the order
    # => Actually, it's the last, as it says "closest to the stack's top when tie"

    def __init__(self):


    def push(self, val: int) -> None:


    def pop(self) -> int:



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end



#
# @lcpr case=start
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]\n
# @lcpr case=end

#

