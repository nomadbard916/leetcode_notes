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
        self.vals: list[int] = []
        self.val_to_idx: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        return True

    def remove(self, val: int) -> bool:
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
