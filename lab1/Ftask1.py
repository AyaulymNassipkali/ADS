n = int(input())

limit = 10000  # достаточно, чтобы покрыть 1000-е простое
prime = [True] * (limit + 1)
prime[0] = prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit + 1, i):
            prime[j] = False

primes = [i for i in range(limit + 1) if prime[i]]
print(primes[n - 1])
