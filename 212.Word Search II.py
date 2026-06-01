#
# @lc app=leetcode id=212 lang=python3
# @lcpr version=30403
#
# [212] Word Search II
#

# @lc code=start
from __future__ import annotations

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        * nouns and verbs
        - m x n board
        - characters
        - list of strings words
        - return all words on the board
        - word: letters of sequentially adjacent cells
        - adjacent cells: horizontally or vertically neighboring
        * pattern kws
        - grid backtracking
        - DFS from each boarad cell
        - keep looking up the same prefix: trie
        - prefix pruning
        - trie for all words
        * constraint kws
        - same letter cell may not be used more than once in a word
        - 1 <= m,n <= 12
        - lower case English letter
        - 1 <= words.length <= 3 * 104
        - 1 <= words[i].length <= 10
        - All the strings of words are unique.
        * map kws to algo
        - matrix/board: backtracking
        - track visited cells during DFS/backtracking
        * mental model
        * tricky kws
        - many words, small board => need shared prefix pruning
        - unique words => no duplicate result output
        - board size small, word list large => optimize by prefix structure
        * pattern specific kws
        - use trie + DFS to prune invalid prefixes early
        - avoid duplicates via trie end-market / visited result set
        """


# @lc code=end


#
# @lcpr case=start
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"]]\n["abcb"]\n
# @lcpr case=end

#
