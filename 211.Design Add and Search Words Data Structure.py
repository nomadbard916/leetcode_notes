#
# @lc app=leetcode id=211 lang=python3
# @lcpr version=30403
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        # 26 slots for 'a'–'z'; None means child doesn't exist
        self.children: list[TrieNode | None] = [None] * 26
        self.is_end: bool = False  # marks a complete stored word


class WordDictionary:
    """
    Trie-backed dictionary with wildcard search support.

    addWord  — O(M)
    search   — O(26^W) worst case (W wildcards), O(M) best case (no wildcards)
    """

    # Problem Understanding
    # You are asked to design a class with two operations:
    # - addWord(word) — store a word
    # - search(word) — return True if any stored word matches the pattern;
    # . in the pattern matches any single character
    # The challenge is that . can appear anywhere in the query, meaning you can't simply do prefix lookups —
    # you may have to explore multiple branches at any character position.

    # ─────────────────────────────────────────────
    # Approach 1: Trie + Recursive DFS  (PRIMARY)
    # ─────────────────────────────────────────────
    # Key insight:
    #   A Trie stores characters one level at a time.
    #   For a literal char c → descend into children[c].
    #   For wildcard '.' → try ALL 26 children (branch).
    #   DFS ensures we explore every matching path.
    #
    # Time  — addWord: O(M) where M = word length
    #       — search:  O(M)  for no wildcards
    #                  O(26^W) worst case (all wildcards, W = word length)
    #                  In practice far less: only existing children are tried
    # Space — O(N * M * 26) for N words of avg length M, 26-pointer array per node

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Insert word into the Trie character by character."""
        node = self.root
        for char in word:
            # map 'a'=0 … 'z'=25
            idx = ord(char) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Return True if word exists in the dictionary.
        '.' matches any single character.
        """
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: str, idx: int, node: TrieNode) -> bool:
        """
        DFS through the Trie matching word[idx:] against subtree rooted at node.

        Base case : idx == len(word) → we consumed the full pattern;
                    success iff this node marks a complete word.
        Wildcard  : try every non-None child recursively.
        Literal   : follow the single matching child (if it exists).
        """
        # ending condition
        if idx == len(word):
            return node.is_end

        ch = word[idx]

        # ── wildcard '.' ────────────────────────────────────────────────────────
        if ch == ".":
            # Branch into every existing child; short-circuit on first match
            for child in node.children:
                if child is not None and self._dfs(word, idx + 1, child):
                    return True
            return False

        # ── literal character ────────────────────────────────────────────────────
        child_idx = ord(ch) - ord("a")
        child = node.children[child_idx]
        if child is None:
            return False

        return self._dfs(word, idx + 1, child)

        # Key Insights
        # - Why Trie and not a hash set?
        # A hash set is O(1) for exact lookup, but when . appears in the middle (e.g. "b.d"),
        # you'd have to compare the pattern against every stored word using regex — O(N·M).
        # A Trie naturally mirrors the character-by-character structure of the problem.
        # - The wildcard = branching decision.
        # In a standard Trie search, at each position you follow exactly one child pointer.
        # When you hit ., you must follow all existing children.
        # This is DFS with branching — and since only existing children are tried,
        # the realistic branching factor is much lower than 26.
        # The worst case O(26^W) only occurs with patterns like "....." against a very dense dictionary.
        # - is_end vs. depth.
        # A common mistake is returning True just because you reached a node at the right depth.
        # You must also check is_end = True. The word "ba" and "bad" both exist as paths in the same Trie;
        # is_end is the only thing that distinguishes them.
        # - BFS vs DFS.
        # Both iterate over the same state space. DFS (recursion) short-circuits on the first match and
        # is natural for sequential pattern matching.
        # BFS (frontier set) is easier to reason about iteratively and
        # avoids deep call stacks for very long words with many wildcards.


# ──────────────────────────────────────────────────────────────────────────────
# Approach 2: Trie + Iterative BFS using a frontier set
# ──────────────────────────────────────────────────────────────────────────────
# Instead of call-stack recursion, maintain a set of "currently active nodes."
# At each character position, advance every node in the frontier.
# For '.' advance to ALL children; for a literal, advance to the one child.
#
# Advantage  : no call-stack overhead; easier to reason about in iterative style
# Disadvantage: set overhead; slightly more memory at peak
#
# Time / Space: same asymptotic as Approach 1


class WordDictionaryBFS:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        frontier: set[TrieNode] = {self.root}  # active nodes at current depth

        for ch in word:
            next_frontier: set[TrieNode] = set()

            if ch == ".":
                for node in frontier:
                    for child in node.children:
                        if child is not None:
                            next_frontier.add(child)
            else:
                idx = ord(ch) - ord("a")
                for node in frontier:
                    child = node.children[idx]
                    if child is not None:
                        next_frontier.add(child)

            if not next_frontier:
                return False  # dead end — no paths survive
            frontier = next_frontier

        # After consuming all characters, any node with is_end=True is a match
        return any(node.is_end for node in frontier)


# ──────────────────────────────────────────────────────────────────────────────
# Approach 3: Hash Set + re.fullmatch  (Naive / Baseline)
# ──────────────────────────────────────────────────────────────────────────────
# Store all words in a plain set.
# On search, convert '.' to the regex dot and match every stored word.
#
# addWord : O(M)
# search  : O(N * M)  — N words, each matched against a pattern of length M
# Useful for:  correctness testing; small dictionaries; quick prototyping.
# Unsuitable for: large N or frequent searches (linear scan every time).

import re


class WordDictionaryNaive:
    def __init__(self) -> None:
        self._words: set[str] = set()

    def addWord(self, word: str) -> None:
        self._words.add(word)

    def search(self, word: str) -> bool:
        pattern = re.compile(word)  # '.' is already a regex wildcard — perfect
        return any(pattern.fullmatch(w) for w in self._words)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end


#
# @lcpr case=start
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]\n
# @lcpr case=end

#
