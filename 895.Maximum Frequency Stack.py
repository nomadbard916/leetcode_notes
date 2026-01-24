#
# @lc app=leetcode id=895 lang=python3
# @lcpr version=30305
#
# [895] Maximum Frequency Stack
#

# @lc code=start
from collections import Counter, defaultdict
from typing import DefaultDict, List


class FreqStack:
    """
    nouns and verbs:
    frequency, stack
    push...top of the stack, pop... remove and return,
    construct
    most frequent element/maximum,
    most recent

    pattern kws: no?

    structural kws:
    most frequent, val might be big int, calls may need to consider performance with 2* 10^4, remove and return, tie: closest to the stack's top

    map to algo:
    frequency & most frequent => counter?

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
        # Track how many times each value appears
        self.freq_counter: Counter[int] = Counter()
        # Group elements by their frequency level
        # freq -> stack of elements with that frequency
        self.group_by_freq: DefaultDict[int, List[int]] = defaultdict(list)
        self.max_freq = 0


    def push(self, val: int) -> None:
        """
        Push a value onto the frequency stack.

        Process:
        1. Increment the frequency of this value
        2. Update max_freq if needed
        3. Add value to the stack at its new frequency level

        Time: O(1)
        """
        self.freq_counter[val]+=1

        freq=self.freq_counter[val]
        self.max_freq:int=max(self.max_freq, freq)

        # Add this value to the stack at its frequency level
        # This naturally maintains "most recent" order within same frequency
        self.group_by_freq[freq].append(val)

    def pop(self) -> int:
        """
        Pop the most frequent element. If tie, pop most recent.

        Process:
        1. Get the stack at max_freq level
        2. Pop from that stack (gives us most recent at that frequency)
        3. Decrement the frequency of that value
        4. If that frequency level is now empty, decrease max_freq

        Time: O(1)
        """
        # Get the most recent element at maximum frequency
        val_to_pop = self.group_by_freq[self.max_freq].pop()
        self.freq_counter[val_to_pop]-=1

        # If no more elements at this frequency level, decrease max_freq; move down when current level is emptied
        if not self.group_by_freq[self.max_freq]:
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

