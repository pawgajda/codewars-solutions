# https://www.codewars.com/kata/5a9996fa8e503f2b4a002e7a
def generate_primes(x):
    if x <= 0:
        return []

    # Sieve of Eratosthenes
    prime = [True] * (x + 1)
    prime[0], prime[1] = False, False

    for i in range(2, int(x**0.5) + 1):
        if prime[i]:
            for j in range(i * i, x + 1, i):
                prime[j] = False

    return [p for p in range(x + 1) if prime[p]]


def odd_not_prime(n):
    odds = [i for i in range(1, n + 1) if i % 2 != 0]
    primes = generate_primes(n)
    
    return len([i for i in odds if i not in primes])
