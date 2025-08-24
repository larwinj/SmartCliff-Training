def func(strings):

    n = len(strings)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(strings[j]) < len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings

user_input = input().split()

res = func(user_input)

print(res)
