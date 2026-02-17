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
        freq_map = Counter(words)
        sorted_words = sorted(freq_map.keys(), key=lambda word: (-freq_map[word], word))
        return sorted_words[:k]

        # ! sol2: heap
        result: List[str] = []
        freq_map = Counter(words)

        heap: List[tuple(int, str)] = []

        for word, freq in freq_map.keys():
            heapq.heappush(heap, (freq, words))

            if len(heap) > k:
                heapq.heappop(heap)

        while heapq:
            result.append(heapq.heappop()[1])

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
