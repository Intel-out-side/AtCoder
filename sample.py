from collections import defaultdict
def factorize(n):
    i = 2
    factors = defaultdict(int)
    while i**2 <= n:
        if n % i != 0:
            i += 1
            continue

        while n % i == 0:
            n //= i
            factors[i] += 1
        i += 1

    if n != 1:
        factors[n] += 1

    return factors

if __name__ == "__main__":
    ans = factorize(int(input()))
    print(ans)
