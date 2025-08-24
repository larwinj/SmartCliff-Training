n = int(input("Enter n: "))
nums = list(map(int,input().split()))

s = set(nums)
m = 0
for n in s:
    if n - 1 not in s:
        l = 1
        while n + 1 in s:
            n += 1
            l += 1
        m = max(m, l)
print(m)