#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for char, count in note_counter.items():
            if char not in magazine_counter:
                return False

            if magazine_counter[char] < count:
                return False

        return True


# @lc code=end
