n = int(input())
elements = [int(input()) for _ in range(n)]

list = []
for x in elements:
    if x not in list:
        list.append(x)

print(list)
