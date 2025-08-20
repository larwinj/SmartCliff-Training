# 20th code :     Count possible ways to construct buildings

MOD = 10**9 + 7
def countWays(n):
    if n == 1:
        return 4

    # Also proved by the base of fibonacci series
    a, b = 1, 2
    for _ in range(3, n+2):
        a, b = b, (a+b) % MOD
    ways_one_side = b

    # Final value be squared
    return (ways_one_side * ways_one_side) % MOD

n = int(input())
print(countWays(n))