#!/usr/bin/python3
"""
This is a prime game module
"""


def isWinner(x, nums):
    """
    This function returns the name of the player that won the most rounds
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def count_primes(n):
        count = 0
        for i in range(1, n + 1):
            if is_prime(i):
                count += 1
        return count

    if sum(map(count_primes, nums)) % 2 == 0:
        return "Ben"
    return "Maria"
