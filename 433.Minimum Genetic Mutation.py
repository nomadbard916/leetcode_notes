#
# @lc app=leetcode id=433 lang=python3
# @lcpr version=30201
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # ! each position has 4 variations => 4-ary tree
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        ACGT_LIST = ["A", "C", "G", "T"]

        # * BFS framework
        def get_all_mutations(gene: str) -> List[str]:
            res = []
            gene_chars = list(gene)
            for i in range(len(gene_chars)):
                old_char = gene_chars[i]
                for new_char in ACGT_LIST:
                    gene_chars[i] = new_char
                    res.append("".join(gene_chars))
                gene_chars[i] = old_char
            return res

        q = deque()
        visited = set()
        q.append(startGene)
        visited.add(startGene)
        steps = 0
        while q:
            q_size = len(q)
            for i in range(q_size):
                cur_node = q.popleft()
                if cur_node == endGene:
                    return steps
                # check surrounding nodes
                for newGene in get_all_mutations(cur_node):
                    if newGene not in visited and newGene in bank_set:
                        q.append(newGene)
                        visited.add(newGene)
            steps += 1
        return -1


# @lc code=end


#
# @lcpr case=start
# "AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]\n
# @lcpr case=end

#
