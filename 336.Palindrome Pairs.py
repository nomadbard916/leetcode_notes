#
# @lc app=leetcode id=336 lang=python3
# @lcpr version=30201
#
# [336] Palindrome Pairs
#

# @lc code=start
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        result = []

        def is_palindrome(s: str) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if is_palindrome(left):
                    reversed_right = right[::-1]
                    if reversed_right in word_map and word_map[reversed_right] != i:
                        result.append([word_map[reversed_right], i])

                if j != len(word) and is_palindrome(right):
                    reversed_left = left[::-1]
                    if reversed_left in word_map and word_map[reversed_left] != i:
                        result.append([i, word_map[reversed_left]])
        return result


# @lc code=end


#
# @lcpr case=start
# ["abcd","dcba","lls","s","sssll"]\n
# @lcpr case=end

# @lcpr case=start
# ["bat","tab","cat"]\n
# @lcpr case=end

# @lcpr case=start
# ["a",""]\n
# @lcpr case=end

#
