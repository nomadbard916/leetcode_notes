#
# @lc app=leetcode id=692 lang=python3
# @lcpr version=30305
#
# [692] Top K Frequent Words
#

# @lc code=start
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        * n & v
        input: array of strings, integer k
        output: k most frequent strings

        return
        sorted
        frequency

        linear search, maybe twice or more?

        * pattern kws
        k most frequent
        dict?
        counter?

        * constraint kws
        frequency highest to lowest
        same frequency: sort by lexicographical order
        words length 1~500, should be fine
        word length 1~10, should be fine
        k 1~500

        * map to algo concepts and build mental category
        heap
        what data structure to store? (freq, val)?

        * tricky kws
        follow up: O(n log(k)) time and O(n) space

        * problem specific pattern kws
        """
        # ! sol1: naive counter
        """
        Main solution using sorting approach.

        Time Complexity: O(n log n) where n is unique words
        Space Complexity: O(n) for the frequency counter

        Args:
            words: List of strings
            k: Number of top frequent words to return

        Returns:
            List of k most frequent words sorted by frequency (desc)
            and lexicographically (asc)
        """
        # Step 1: Count frequency of each word
        freq_map = Counter(words)

        # Step 2: Sort by two criteria
        # Primary: frequency (descending) → use negative for desc order
        # Secondary: word itself (ascending) → lexicographical order
        sorted_words = sorted(freq_map.keys(), key=lambda word: (-freq_map[word], word))

        # Step 3: Return first k elements
        return sorted_words[:k]

        # ! sol2: heap
        """
        Heap solution using max-heap behavior via negation.

        Time Complexity: O(n + m log m) where n is total words, m is unique words
        Space Complexity: O(m) for frequency map and heap

        Key insight: Use negative frequency to simulate max-heap behavior.
        Python's heapq is a min-heap, so:
        - Negate frequency: -freq makes higher frequencies come out first
        - Lexicographical order: When -freq ties, Python compares word naturally

        This is simpler and more elegant than maintaining a size-k heap!
        """
        result: List[str] = []

        # Step 1: Count frequencies
        freq_map = Counter(words)

        # Step 2: Build heap with all words
        # Tuple: (-freq, word)
        # - Negative freq for max-heap behavior (higher freq = smaller -freq value)
        # - Word for lexicographical tie-breaking
        heap: List[tuple(int, str)] = []
        for word, freq in freq_map.items():
            # Negate frequency to get max-heap behavior
            # When frequencies tie, Python automatically compares words lexicographically
            heapq.heappush(heap, (-freq, word))

        # Step 3: Pop k elements
        # They come out in descending frequency order
        # With lexicographical order for ties
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        # ! sol3 heap most optimized
        """
        Optimized O(n log k) solution using size-k min-heap with custom comparator.

        Time Complexity: O(n log k) where n is total words
        Space Complexity: O(n) for frequency map + O(k) for heap

        Key insight: Maintain a heap of size k.
        We want to KEEP the k largest items (highest freq, smallest word when tie).
        So we EVICT the smallest items (lowest freq, largest word when tie).

        For a min-heap, the smallest item is at top and gets popped.
        So we define "smallest" as what we want to evict!
        """
        freq_map = Counter(words)

        class WordFreq:
            def __init__(self, word: str, freq: int):
                self.word = word
                self.freq = freq

            def __lt__(self, other: "WordFreq") -> bool:
                """
                Define "less than" for min-heap comparison.
                "Smaller" items get evicted when heap exceeds k.

                We want to KEEP:
                - High frequency words
                - Lexicographically smaller words when freq ties

                So we want to EVICT (define as "smaller"):
                - Low frequency words
                - Lexicographically larger words when freq ties
                """
                if self.freq != other.freq:
                    return self.freq < other.freq  # Lower freq is "smaller"
                return self.word > other.word  # Larger word is "smaller"

            def __repr__(self) -> str:
                return f"{self.word}:{self.freq}"

        heap: List[WordFreq] = []

        for word, freq in freq_map.items():
            heapq.heappush(heap, WordFreq(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract and sort the result
        # Heap is in arbitrary order, so we need to sort properly
        result = sorted(heap, key=lambda x: (-x.freq, x.word))
        return [item.word for item in result]


# @lc code=end


#
# @lcpr case=start
# ["i","love","leetcode","i","love","coding"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["the","day","is","sunny","the","the","the","sunny","is","is"]\n4\n
# @lcpr case=end

#
