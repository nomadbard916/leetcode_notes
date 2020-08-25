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

        # sanity check
        if n <= 2:
            return 0

        is_prime: list = [1] * n
        is_prime[0], is_prime[1] = 0, 0

        # from first prime (2) to sqrt(n)+1
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i] == 1:
                # mark all the multiples of this prime to be non-prime,
                #  starting from square of it
                is_prime[i * i : n : i] = [0] * len(is_prime[i * i : n : i])

        return sum(is_prime)


# @lc code=end

