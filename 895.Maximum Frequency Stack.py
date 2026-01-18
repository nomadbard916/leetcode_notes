#
# @lc app=leetcode id=895 lang=python3
# @lcpr version=30305
#
# [895] Maximum Frequency Stack
#

# @lc code=start
from collections import Counter, defaultdict


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

    # how to make test:
    """
    1. push once
    2. pop once
    3. push thrice with freq (2,1)
    4. pop to check the one with freq 2 is popped
    """

    def __init__(self):
        self.freq_counter=Counter()
        self.freq_vals_map = defaultdict(list)
        self.max_freq = 0


    def push(self, val: int) -> None:
        self.freq_counter[val]+=1
        f=self.freq_counter[val]
        self.freq_vals_map[f].append(val)
        self.max_freq=max(self.max_freq, f)



    def pop(self) -> int:
        # check from the freq_counter
        val_to_pop = self.freq_vals_map[self.max_freq].pop()
        self.freq_counter[val_to_pop]-=1
        if not self.freq_vals_map[self.max_freq]:
            self.max_freq-=1
        return val_to_pop



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

