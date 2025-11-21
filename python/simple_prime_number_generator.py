# https://www.codewars.com/kata/58fa5e33a6d84c1324000207
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
