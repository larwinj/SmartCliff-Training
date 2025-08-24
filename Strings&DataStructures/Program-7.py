import collections

n = int(input())
nums = [int(input()) for _ in range(n)]

ans = 0

#dict by mapping the values with its frequency.
count = collections.Counter()

for i in range(len(nums)):
    for j in range(i):
        prod = nums[i] * nums[j]
        #All combinations can have 8 possible outcomes because the size of the valid tuple is 4
        ans += count[prod] * 8
        count[prod] += 1

print(ans)