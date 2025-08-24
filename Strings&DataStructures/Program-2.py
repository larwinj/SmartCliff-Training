def func(s):
    lower = ""
    upper = ""
    for ch in s:
        if ch.islower():
            lower += ch
        else:
            upper += ch
    return lower + upper

s = input("str1 = ")
print(func(s))
