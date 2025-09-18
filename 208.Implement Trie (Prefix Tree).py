#
# @lc app=leetcode id=208 lang=python3
# @lcpr version=30201
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
    def __init__(self) -> None:
        """
            A node in the Trie data structure.
            Each node contains:
        - children: dictionary mapping characters to child nodes
        - is_end_of_word: boolean indicating if this node represents the end of a word
        """
        self.children: dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False


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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
