#
# @lc app=leetcode id=211 lang=python3
# @lcpr version=30403
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start


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
        for ch in word:
            idx = ord(ch) - ord("a")
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
        if idx == len(word):
            return node.is_end

        ch = word[idx]

        if ch == ".":
            for child in node.children:
                if child is not None and self._dfs(word, idx + 1, child):
                    return True
            return False

        child_idx = ord(ch) - ord("a")
        child = node.children[child_idx]
        if child is None:
            return False
        return self._dfs(word, idx + 1, child)


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
