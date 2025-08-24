def find(n, nums):
    nums_set = set(nums)
    res = []

    for i in range(1, n + 1):
        if i not in nums_set:
            res.append(i)  # add missing number

    return res

n = int(input())
nums = list(map(int, input().split()))

result = find(n, nums)
print(result)