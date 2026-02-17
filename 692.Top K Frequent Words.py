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
        Alternative solution using Min-Heap (more optimal for large datasets).

        Time Complexity: O(n log k) where n is total words
        Space Complexity: O(n) for frequency map + O(k) for heap

        Key insight: Maintain a min-heap of size k.
        For min-heap, we want to keep the LARGEST k items,
        so we evict the SMALLEST when heap size exceeds k.

        Python's heapq is a min-heap, so we need to reverse the comparison:
        - For frequency: use positive (smaller freq gets evicted)
        - For lexicographical: use reverse (larger alphabetically gets evicted)
        """
        result: List[str] = []

        # Step 1: Count frequencies
        freq_map = Counter(words)

        # Step 2: Use min-heap with size k
        # Heap element: (freq, reverse_word, word)
        # We want to keep high frequency, so low frequency gets popped
        # We want to keep lexicographically smaller, so larger gets popped
        heap: List[tuple(int, str)] = []

        for word, freq in freq_map.keys():
            # For min-heap to keep top K:
            # - Use positive freq (smaller freq = smaller priority = gets evicted)
            # - Use reverse of word (larger word = sm
            heapq.heappush(heap, (freq, word))

            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract and sort result
        # Pop from heap and reverse order
        # Since heap pops in ascending order of (freq, word),
        # we need to reverse to get descending frequency
        while heapq:
            result.append(heapq.heappop()[1])

        # Reverse to get highest frequency first
        result.reverse()

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
