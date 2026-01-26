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

    pattern kws:
    design
    max freq => need to track counts
    most recently pushed => order matters, LIFO for ties

    structural kws:
    most frequent, val might be big int, calls may need to consider performance with 2* 10^4, remove and return, tie: closest to the stack's top

    map to algo:
    frequency & most frequent => counter?

    mental category: no?

    tricky kws:
    "Most recently pushed among them" → Not just max frequency, but LIFO within same frequency

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
        # The Challenge:
        # Traditional stack can't do this because it doesn't track frequencies.
        # A simple frequency counter can't do this because it loses the "most recent" information.

        # Track how many times each value appears
        self.freq_counter: Counter[int] = Counter()
        # Group elements by their frequency level
        # freq -> stack of elements with that frequency
        # Each element can exist at multiple frequency levels simultaneously!
        self.freq_group_map: DefaultDict[int, List[int]] = defaultdict(list)

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
        self.freq_group_map[freq].append(val)

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
        val_to_pop = self.freq_group_map[self.max_freq].pop()
        self.freq_counter[val_to_pop]-=1

        # If no more elements at this frequency level, decrease max_freq; move down when current level is emptied
        if not self.freq_group_map[self.max_freq]:
            self.max_freq-=1

        return val_to_pop

        # Complexity Analysis
        # - Time Complexity:
        # push(): O(1) - hash map updates and list append
        # pop(): O(1) - list pop and hash map update

        # - Space Complexity:
        # O(n) where n is total number of elements pushed
        # Each element creates at most one entry per frequency level
        # In worst case, if all elements are the same, that element appears at freq levels 1, 2, 3...n

        """
        Q: I don't understand this: "If no more elements at this frequency level, decrease max_freq"

        Great question! Let me break this down step-by-step with a concrete example.

        ## The Scenario

        Imagine this sequence:

        ```python
        freq_stack = FreqStack()
        freq_stack.push(5)  # 5 appears 1 time
        freq_stack.push(5)  # 5 appears 2 times
        freq_stack.push(5)  # 5 appears 3 times
        ```

        **After these pushes, our data structures look like:**

        ```
        freq_map = {5: 3}

        group_by_freq = {
            1: [5],    # 5's first occurrence
            2: [5],    # 5's second occurrence
            3: [5]     # 5's third occurrence
        }

        max_freq = 3   # The highest frequency level that has elements
        ```

        ---

        ## Now Let's Pop

        ### **First pop():**

        ```python
        val = freq_stack.pop()  # Returns 5
        ```

        **What happens:**

        1. We look at `group_by_freq[3]` (the max_freq level)
        2. We pop from it: `group_by_freq[3].pop()` returns `5`
        3. Now `group_by_freq[3]` is **empty** `[]`
        4. We decrement `freq_map[5]` from 3 to 2

        **HERE'S THE KEY PART:**
        ```python
        if not self.group_by_freq[self.max_freq]:  # Is group_by_freq[3] empty?
            self.max_freq -= 1  # Yes! So decrease max_freq from 3 to 2
        ```

        **After first pop:**
        ```
        freq_map = {5: 2}

        group_by_freq = {
            1: [5],
            2: [5],
            3: []      # EMPTY!
        }

        max_freq = 2   # Decreased from 3 to 2
        ```

        ---

        ### **Second pop():**

        ```python
        val = freq_stack.pop()  # Returns 5
        ```

        1. Look at `group_by_freq[2]` (current max_freq)
        2. Pop from it: returns `5`
        3. Now `group_by_freq[2]` is **empty** `[]`
        4. Decrement `freq_map[5]` from 2 to 1
        5. Check: is `group_by_freq[2]` empty? **Yes!**
        6. Decrease `max_freq` from 2 to 1

        **After second pop:**
        ```
        freq_map = {5: 1}

        group_by_freq = {
            1: [5],
            2: [],     # EMPTY!
            3: []      # EMPTY!
        }

        max_freq = 1   # Decreased from 2 to 1
        ```

        ---

        ## Why Is This Necessary?

        **Without decreasing max_freq:**

        If we kept `max_freq = 3` after the first pop, what would happen on the second pop?

        ```python
        # BAD - if we didn't decrease max_freq:
        val = self.group_by_freq[3].pop()  # ERROR! group_by_freq[3] is empty!
        ```

        We'd try to pop from an empty list → **crash!**

        ---

        ## Audio-Oriented Analogy

        Think of a **parking garage with multiple floors:**

        - Floor 1 (freq 1): has some cars
        - Floor 2 (freq 2): has some cars
        - Floor 3 (freq 3): has some cars

        **max_freq is like an elevator that always goes to the highest occupied floor.**

        When you retrieve a car:
        1. Elevator goes to floor 3 (max_freq)
        2. You take a car from floor 3
        3. **If floor 3 is now empty**, the elevator needs to go down to floor 2 next time
        4. So we update: "highest occupied floor is now 2" (max_freq = 2)

        **If we didn't update this:**
        - Next time we'd send the elevator to floor 3
        - But floor 3 is empty!
        - Elevator opens to... nothing! (crash)

        ---

        ## More Complex Example

        Let's see when max_freq does NOT decrease:

        ```python
        freq_stack = FreqStack()
        freq_stack.push(5)
        freq_stack.push(7)
        freq_stack.push(5)
        freq_stack.push(7)
        freq_stack.push(5)  # 5 appears 3 times
        ```

        **State:**
        ```
        freq_map = {5: 3, 7: 2}

        group_by_freq = {
            1: [5, 7],
            2: [5, 7],
            3: [5]
        }

        max_freq = 3
        ```

        **Now pop():**

        1. Pop from `group_by_freq[3]` → returns `5`
        2. `group_by_freq[3]` is now empty `[]`
        3. Decrease max_freq to 2 ✓

        **Second pop():**

        1. Pop from `group_by_freq[2]` → returns `7` (most recent at freq 2)
        2. `group_by_freq[2]` is now `[5]` - **NOT EMPTY!**
        3. **Do NOT decrease max_freq** (stays at 2) ✓

        ```
        freq_map = {5: 2, 7: 1}

        group_by_freq = {
            1: [5, 7],
            2: [5],    # Still has element 5!
            3: []
        }

        max_freq = 2   # Stays at 2 because group_by_freq[2] still has elements
        ```

        ---

        ## The Rule in Simple Terms

        **"If no more elements at this frequency level, decrease max_freq"** means:

        > After popping, if the stack at the current max_freq level is now empty, we need to move down to the next frequency level. Otherwise, the next pop() would try to access an empty stack.

        It's like maintaining a "water level" - when you drain the top level completely, the water level drops to the next occupied level below.

        ---

        Does this clarify it? The key insight is: **max_freq must always point to a non-empty frequency level** (or be 0 if everything is empty).
        """



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

