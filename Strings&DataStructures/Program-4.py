n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

element = int(input())

if element in arr:
    print("True")
else:
    print("False")