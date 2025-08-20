# 22th code :

n = int(input())

steps = 0
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    # Incrementing the count value for every iteration
    steps += 1

print(steps)