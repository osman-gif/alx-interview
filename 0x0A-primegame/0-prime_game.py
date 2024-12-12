def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i*i, max_n + 1, i):
                sieve[multiple] = False

    prime_counts = [0] * (max_n + 1)
    count = 0
    for i in range(1, max_n + 1):
        if sieve[i]:
            count += 1
        prime_counts[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        if n < 2:
            ben_wins += 1
            continue
        primes = prime_counts[n]
        if primes % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
