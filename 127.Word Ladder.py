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
        # ! sol1: plain BFS
        # use BFS as it's about "shortest path"
        # so it's faster than backtrack even as both are essentially brute force

        # this one is pretty much like lc 752 open the lock

        # Convert wordList to set for O(1) lookup
        word_set = set(wordList)

        # If endWord is not in wordList, transformation is impossible
        if endWord not in word_set:
            return 0

        # BFS queue: each element is (current_word, steps_taken)
        q = deque([(beginWord, 1)])

        # Set to track visited words to avoid cycles
        visited: Set[str] = {beginWord}

        while q:
            current_word, steps = q.popleft()

            # Try changing each character position
            for i in range(len(current_word)):
                # Try all 26 possible letters at position i
                for c in "abcdefghijklmnopqrstuvwxyz":
                    # Skip if it's the same character
                    if c == current_word[i]:
                        continue

                    # Create new word by replacing character at position i
                    new_word = current_word[:i] + c + current_word[i + 1 :]

                    # Check if we reached the target
                    if new_word == endWord:
                        return steps + 1

                    # If new_word is valid and unvisited, add to queue
                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, steps + 1))

        # No transformation sequence found
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

        # ! sol2: bi-directional BFS
        # it's under the same time and space complexity but faster.
        # it's searches from both ends simultaneously. This can significantly reduce the search space:
        # - Instead of exploring one large tree, we explore two smaller trees
        # - When they meet, we've found the shortest path
        # - Time complexity remains the same in worst case, but average case is much better
        # - Space complexity is similar but with potential for better cache performance
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # Two sets for bidirectional search
        begin_set = {beginWord}
        end_set = {endWord}

        visited = set()
        steps = 1

        while begin_set and end_set:
            # Always expand the smaller set for better performance
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            next_set = set()
            # If no new words are found, begin_set becomes empty, and the loop exits.
            for word in begin_set:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        new_word = word[:i] + c + word[i + 1 :]

                        # If new_word is in the other search direction, we found a path
                        if new_word in end_set:
                            return steps + 1

                        # Add to next level if it's a valid unvisited word
                        if new_word in word_set and new_word not in visited:
                            visited.add(new_word)
                            next_set.add(new_word)
            begin_set = next_set
            steps += 1
        return 0


# @lc code=end


#
# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]\n
# @lcpr case=end

# @lcpr case=start
# "hit"\n"cog"\n["hot","dot","dog","lot","log"]\n
# @lcpr case=end

#
