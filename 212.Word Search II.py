#
# @lc app=leetcode id=212 lang=python3
# @lcpr version=30403
#
# [212] Word Search II
#

# @lc code=start

from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        # Children map: char → TrieNode
        self.children: dict[str, "TrieNode"] = {}
        # Store the full word string at the terminal node (None if not terminal)
        # Storing the word itself is cleaner than a boolean flag —
        # we can append it to results directly without reconstructing the path.
        self.word: Optional[str] = None


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
        - find: search/locate
        * pattern kws
        - grid backtracking
        - DFS from each boarad cell
        - keep looking up the same prefix: trie
        - prefix pruning
        - trie for all words
        - finding multiple targets simultaneously => trie
        * constraint kws
        - same letter cell may not be used more than once in a word => in-place visited flag
        - 1 <= m,n <= 12
        - lower case English letter
        - 1 <= words.length <= 3 * 104
        - 1 <= words[i].length <= 10
        - All the strings of words are unique.
        * map kws to algo
        - matrix/board: backtracking
        - track visited cells during DFS/backtracking
        - pruning dead branches: remove exhausted trie nodes
        * mental model
        - Brute Force: DFS per word → O(W × M × N × 4^L) — TLE for large inputs
        - Optimal: Build Trie from all words, single DFS pass over board → all words checked simultaneously
        * tricky kws
        - many words, small board => need shared prefix pruning
        - unique words => no duplicate result output
        - board size small, word list large => optimize by prefix structure
        * pattern specific kws
        - use trie + DFS backtracking to prune invalid prefixes early
        - avoid duplicates via trie end-market / visited result set
        """

        # ─────────────────────────────────────────────────────────────
        # Approach 2: Trie + DFS (Optimal)
        # ─────────────────────────────────────────────────────────────
        # Key insight: Instead of searching one word at a time,
        # build a Trie from ALL words, then do ONE DFS pass over the board.
        # At every cell, we navigate the Trie and board simultaneously —
        # the Trie's shared prefix structure prunes huge branches.
        #
        # Extra optimization: After finding a word, prune leaf Trie nodes
        # bottom-up so we don't revisit them. This makes the algorithm
        # significantly faster on dense boards with many short words.

        # ── Step 1: Build the Trie ──────────────────────────────
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                # create child node if it doesn't exist
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word  # mark terminal with full word
        rows, cols = len(board), len(board[0])
        result: list[str] = []

        # ── Step 2: DFS + Backtracking ──────────────────────────
        def dfs(r: int, c: int, parent_node: TrieNode):
            """
            Simultaneously walk the board and the Trie.
            parent_node: the Trie node corresponding to the prefix
                         formed by the path from the DFS root to (r, c).
            """
            ch = board[r][c]
            # base case Prune: if current char not in Trie at this level, dead end
            if ch not in parent_node.children:
                return

            curr_node = parent_node.children[ch]

            # ── Found a complete word ──
            if curr_node.word is not None:
                result.append(curr_node.word)
                # Set to None to prevent duplicate entries
                # (the same word could be found via different paths)
                curr_node.word = None

            # ── Mark visited by corrupting the cell ──
            # This is the backtracking trick: '#' is not a letter,
            # so any DFS branch that reaches here won't re-enter this cell.
            board[r][c] = "#"

            # ── Explore 4 neighbors ──
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, curr_node)

            # ── Restore cell (backtrack) ──
            board[r][c] = ch

            # ── Trie Pruning (the key optimization!) ──────────────
            # If curr_node now has no children AND no word remaining,
            # it is a dead leaf — we'll never need it again.
            # Remove it from its parent to shrink the Trie over time.
            # This prevents re-exploring paths leading to already-found words.
            if not curr_node.children and curr_node.word is None:
                del parent_node.children[ch]

        # ── Step 3: Trigger DFS from every board cell ───────────
        for r in range(rows):
            for c in range(cols):
                # Quick pre-check: only start DFS if this char is
                # a first letter of any word (i.e., in Trie root's children)
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result


# @lc code=end


#
# @lcpr case=start
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"]]\n["abcb"]\n
# @lcpr case=end

#
