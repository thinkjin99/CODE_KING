n = int(input())
if n <= 3:
    print(6)
    exit()
is_prime = [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, n, i):
            is_prime[j] = False
primes = [i for i in range(2, n) if is_prime[i]]
left = 0; right = len(primes)
for i in range(len(primes) - 1):
    multiple = primes[i] * primes[i + 1]
    if multiple > n:
        print(multiple)
        break
