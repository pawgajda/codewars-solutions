https://www.codewars.com/kata/5902ea9b378a92a990000016
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


def sum_primes(lower, upper):
    if lower > upper:
        return 0
    
    primes = generate_primes(upper)
    sum = 0
    
    for i in range(0, len(primes)):
        if primes[i] >= lower and primes[i] <= upper:
            sum += primes[i]
    
    return sum
