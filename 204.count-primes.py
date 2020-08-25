#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        #  sieve of Eratosthenes:
        # the biggest prime factor of n must not exceed sqrt(n)
        # https://ithelp.ithome.com.tw/articles/10223005

        # though it's good, but who can remember it?
        # let's only take the essence of tabulation

        # sanity check
        if n <= 2:
            return 0

        is_prime: list = [True] * n
        is_prime[0], is_prime[1] = False, False

        for i in range(2, n):
            if is_prime[i]:
                # mark all the multiples of i as non-prime
                is_prime[i * 2 : n : i] = [False] * len(is_prime[i * 2 : n : i])

        return sum(is_prime)


# @lc code=end

