def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
limit = int(input("Find all primes up to: "))
primes = [n for n in range(2, limit + 1) if is_prime(n)]
print(f"Found {len(primes)} primes:")
print(primes)