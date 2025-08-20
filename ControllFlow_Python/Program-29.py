# 29th Code :

def kap(num):
    target = 6174
    count = 0

    while num != target:
        d = f"{num:04d}"
        l = int("".join(sorted(d, reverse=True)))
        s = int("".join(sorted(d)))
        num = l - s
        count += 1
    return count


print(kap(int(input())))