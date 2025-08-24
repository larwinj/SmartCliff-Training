def func():
    n = int(input())

    element = input()
    arr = []
    for _ in range(n):
        arr.append(input())
    count = 0
    for item in arr:
        # checking of the numbers
        if item == element:
            count += 1
    print(count)

func()