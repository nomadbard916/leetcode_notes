#
# @lc app=leetcode id=380 lang=python3
# @lcpr version=30201
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:
    # nouns and verbs
    """
    - set (DS)
    - randomized
    - insert
    - remove
    - getRandom
    - probability (same)
    """

    # pattern KWs
    """
    - getRandom() -> random access
    - O(1) time complexity -> constant time operations
    - insert, remove -> DS modification
    - each element must have the same probability -> uniform distribution
    """

    # constraint
    """
    - insert if not present , return true if not present, false otherwise
    - remove if present, return true if present, false otherwise
    - guaranteed element exist when getRandom() called
    - O(1)
    - val range very big, in full integer range
    - at most 2 * 10^5 calls for each function -> need efficient operations
    """

    # KW -> algo map
    """
    - O(1) insert -> hash set/ hash map / array append
    - O(1) remove -> hash set/ hash map
    - O(1) getRandom -> array (random index access)
    - same probability -> contiguous index access

    - but hash sets have O(1) insert/remove, not O(1) random access
    - arrays have O(1) random access, but O(n) remove (shifting elements)
    """

    # mental categories
    """
    design: hash map + array
    """

    # tricky keywords
    """
    - getRandom... same probability -> can't use hash set alone (no index)
    - O(1) remove -> can't use array alone (shift O(n))
    """

    def __init__(self):
        # List stores actual values - enables O(1) random access
        self.vals: list[int] = []
        # HashMap stores value -> index mapping - enables O(1) lookup
        self.val_to_idx: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        """
        Insert val if not present.
        Returns True if inserted, False if already exists.

        Time: O(1) average
        """
        if val in self.val_to_idx:
            return False

        # add to the end of list and record its index
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Remove val if present.
        Returns True if removed, False if not found.

        Key trick: Swap with last element to achieve O(1) removal.

        Time: O(1) average
        """
        if val not in self.val_to_idx:
            return False

        # Get index of element to remove
        idx_to_remove = self.val_to_idx[val]
        last_val = self.vals[-1]

        # Step 1: Move last element to the position of element to remove
        self.vals[idx_to_remove] = last_val
        self.val_to_idx[last_val] = idx_to_remove

        # Step 2: Remove the last element (now a duplicate)
        self.vals.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
