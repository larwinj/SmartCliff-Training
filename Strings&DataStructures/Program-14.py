n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()

if n % 2 == 1:
    median = nums[n // 2]
else:
    median = (nums[n // 2 - 1] + nums[n // 2]) / 2

print(median)
