#
# @lc app=leetcode id=336 lang=python3
# @lcpr version=30201
#
# [336] Palindrome Pairs
#

# @lc code=start
from typing import List


class Solution:
    # Key Insight:
    # Instead of checking every pair (O(n²) pairs × O(k) palindrome check = O(n²k)),
    # we use a hash map to find matching words efficiently.
    # The Core Idea:
    # For a word to form a palindrome when concatenated with another word,
    # we need to split it and check if parts can match with reversed versions of other words.
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Find all pairs of indices (i, j) where words[i] + words[j] forms a palindrome.

        Strategy:
        1. Store all words with their indices in a hashmap (reversed word -> index)
        2. For each word, check all possible splits:
           - If left part is palindrome, check if reversed right part exists
           - If right part is palindrome, check if reversed left part exists
        3. Handle special cases like empty strings
        """
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
            # Check all possible splits of current word
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                # Case 1: If left part is palindrome
                # We need reversed(right) to exist as another word
                # When we concatenate: reversed(right) + word, it forms a palindrome
                if is_palindrome(left):
                    reversed_right = right[::-1]
                    if reversed_right in word_map and word_map[reversed_right] != i:
                        result.append([word_map[reversed_right], i])

                # Case 2: If right part is palindrome
                # We need reversed(left) to exist as another word
                # When we concatenate: word + reversed(left), it forms a palindrome
                # Use j != len(word) to avoid duplicate when right is empty
                if j != len(word) and is_palindrome(right):
                    reversed_left = left[::-1]
                    if reversed_left in word_map and word_map[reversed_left] != i:
                        result.append([i, word_map[reversed_left]])
        return result

    #     Time Complexity: O(n × k²)
    # n = number of words
    # k = average length of words
    # For each word: O(k) splits × O(k) palindrome check = O(k²)
    # Total: O(n × k²)

    # Space Complexity: O(n × k)
    # Hash map stores n words, each of length k
    # Result list: at most O(n²) pairs in worst case


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
