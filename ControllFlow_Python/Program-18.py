# 18th code  (Legendre’s formula:)       Factorial Divisibility

def largest_power(n, p):
    pow = 0
    div = p

    # It can proved by the formulae of n/p + n/p^2 + n/p^3 ...
    while div <= n:
        pow += n // div
        div *= p
    return pow

n = int(input())
p = int(input())

print(largest_power(n, p))
