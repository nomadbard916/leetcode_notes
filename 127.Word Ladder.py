#
# @lc app=leetcode id=127 lang=python3
# @lcpr version=30201
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
from typing import List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # use BFS as it's about "shortest path"
        # so it's faster than backtrack even as both are essentially brute force

        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])

        visited: Set[str] = {beginWord}

        while q:
            current_word, steps = q.popleft()

            for i in range(len(current_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == current_word[i]:
                        continue

                    new_word = current_word[:i] + c + current_word[i + 1 :]

                    if new_word == endWord:
                        return steps + 1

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, steps + 1))

        return 0

        # Time Complexity: O(M² × N)

        # M = length of each word
        # N = total number of words in wordList
        # For each word, we try M positions × 26 letters = O(M × 26)
        # Creating each new word takes O(M) time
        # In worst case, we visit all N words

        # Space Complexity: O(M × N)

        # Queue can store up to N words, each of length M
        # Visited set can store up to N words
        # Word set stores N words of length M each


# @lc code=end


#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#
