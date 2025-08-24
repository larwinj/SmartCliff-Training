n = int(input())
nums = [int(input()) for _ in range(n)]

positive = []
negative = []

for num in nums:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

print("Original List:", nums)
print("Positive List:", positive)
print("Negative List:", negative)
