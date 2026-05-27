#
# @lc app=leetcode id=208 lang=python3
# @lcpr version=30201
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from __future__ import annotations


class TrieNode:
    def __init__(self) -> None:
        """
            A node in the Trie data structure.
            Each node contains:
        - children: dictionary mapping characters to child nodes
        - is_end_of_word: boolean indicating if this node represents the end of a word
        """
        # Why the array wins over hashmap for storing children here — and when it doesn't
        # 1. Access time
        # Array: children[ord(ch) - ord('a')] is O(1) with a tiny constant — it's a direct memory offset. No hashing, no collision resolution.
        # HashMap: also amortized O(1), but involves computing a hash, checking for collisions, and potentially a second memory hop. The constant is meaningfully larger.
        # For Trie operations that traverse character by character, this per-node cost adds up.
        # 2. Space per node
        # Array: always allocates 26 pointers, regardless of how many children actually exist. Each None slot still occupies memory (8 bytes on 64-bit Python). That's 208 bytes per node minimum.
        # HashMap: only stores existing children. A node with 2 children takes ~2 entries of overhead, not 26.
        # 3. 3. Wildcard iteration
        # This is the critical one for LC 211. When you hit ., you need to iterate all children
        self.children: dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False

        # Condition,Preferred Data Structure
        # Alphabet is small & fixed (a–z),Array
        # "Alphabet is large (Unicode, full ASCII)",HashMap
        # "Trie is dense (short words, shared prefixes)",Array
        # "Trie is sparse (long words, few prefixes)",HashMap
        # Frequent wildcard search over sparse nodes,HashMap
        # Simplicity & cache locality matter,Array


class Trie:
    def __init__(self):
        """Initialize the Trie with an empty root node."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
            word: The word to insert

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(m) in worst case (when no prefixes exist)
        """
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Search for a complete word in the Trie.

        Args:
            word: The word to search for

        Returns:
            True if the word exists in the Trie, False otherwise

        Time Complexity: O(m) where m is the length of the word
        Space Complexity: O(1) - only uses a constant amount of extra space
        """
        current = self.root

        for char in word:
            # If character doesn't exist, word is not in Trie
            if char not in current.children:
                return False
            current = current.children[char]

        # Return True only if we've reached the end of a complete word
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Check if any word in the Trie starts with the given prefix.

        Args:
            prefix: The prefix to search for

        Returns:
            True if any word starts with the prefix, False otherwise

        Time Complexity: O(m) where m is the length of the prefix
        Space Complexity: O(1) - only uses a constant amount of extra space
        """
        current = self.root

        for char in prefix:
            # If character doesn't exist, no word has this prefix
            if char not in current.children:
                return False
            current = current.children[char]

        # If we successfully traversed the prefix, it exists
        return True

        # complexity
        # Approach,addWord,search (no wildcards),search (all wildcards),Space
        # Trie + DFS,O(M),O(M),O(26^W) worst,O(N·M·26)
        # Trie + BFS,O(M),O(M),O(26^W) worst,O(N·M·26)
        # Hash set + regex,O(M),O(N·M),O(N·M),O(N·M)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
