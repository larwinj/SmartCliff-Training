# 28th Code :


# Finding the prime number or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def circular(n):
    s = str(n)
    for i in range(len(s)):
        rotated = int(s[i:] + s[:i])
        # print(rotated)
        if not is_prime(rotated):
            return "NO"
    return "YES"

print(circular(int(input())))