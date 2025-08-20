# 26th code :


def func(n):
    width = 2 * n + 2

    print("*" * width)

    for i in range(n, 0, -1):
        l = "*" * i
        m = " " * (width - 2*i)
        r = "*" * i
        print(l + m + r)

    print("*" * width)

func(int(input()))
