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
        Alternative solution using Max-Heap (more optimal for large datasets).

        Time: O(n + m log m + k log m)
        - O(n) for Counter
        - O(m log m) for pushing m unique words into heap
        - O(k log m) for popping k items
        - Since we push ALL words, this simplifies to O(n + m log m)

        Space: O(m) for freq_map + O(m) for heap = O(m)

        Key insight: Maintain a max-heap
        word is still in ascending order, so when popping from heap,
        the lexicographically smaller one is popped
        """
        result: List[str] = []

        # Step 1: Count frequencies
        freq_map = Counter(words)

        # Step 2: Use heap, freq for max heap behavior and word for min
        heap: List[tuple(int, str)] = []
        for word, freq in freq_map.items():
            # For min-heap to keep top K:
            # Use negative freq for max-heap behavior, but this alone isn't enough
            # word remains unchanged as lexicographical order is considered in min-heap behavior
            heapq.heappush(heap, (-freq, word))

        # Step 3: Extract and sort result
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

        # ! sol3 heap most optimized
        """
        Most optimized heap solution with proper custom comparison.

        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """
        freq_map = Counter(words)

        # Python's heapq creates min-heap
        # We want to maintain k largest items (by our custom criteria)
        # So the "smallest" item (by our criteria) should be evicted

        # Custom comparison for min-heap:
        # - Lower frequency should be evicted → use +freq
        # - When freq ties, lexicographically larger should be evicted → use reverse

        class WordFreq:
            def __init__(self, word: str, freq: int):
                self.word = word
                self.freq = freq

            def __lt__(self, other: "WordFreq") -> bool:
                # Define "less than" for min-heap
                # Smaller items get evicted when heap exceeds k
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

        # Extract words and reverse (heap gives ascending order)
        result = [item.word for item in sorted(heap, reverse=True)]
        return result


# @lc code=end


#
# @lcpr case=start
# ["i","love","leetcode","i","love","coding"]\n2\n
# @lcpr case=end

# @lcpr case=start
# ["the","day","is","sunny","the","the","the","sunny","is","is"]\n4\n
# @lcpr case=end

#
