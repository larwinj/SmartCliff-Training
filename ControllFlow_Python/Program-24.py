# 24th code :

def dfs(n, k):
    ar = list(range(1, n + 1))
    # print(ar)
    index = 0

    while len(ar) > 1:
        index = (index + k - 1) % len(ar)
        ar.pop(index)

    return ar[0]

print(dfs(int(input()), int(input())))

