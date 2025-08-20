# 25th code :

def func(n):
    for i in range(1, n + 1):

        # It is for spacing loop
        for j in range(n - i):
            print(" ", end=" ")

        # Firstlevel
        num = i
        for k in range(1, i + 1):
            print(num, end=" ")
            num += 1

        # SecondLevel
        num -= 2
        for k in range(1, i):
            print(num, end=" ")
            num -= 1

        print()

func(int(input()))
