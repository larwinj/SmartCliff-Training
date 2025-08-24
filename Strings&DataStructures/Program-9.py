def find(nums):
    n = len(nums)
    seen = set()
    duplicate = -1

    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)

    # missing number
    for i in range(1, n + 1):
        if i not in seen:
            missing = i
            break

    return duplicate, missing

n = int(input())
nums = list(map(int, input().split()))

dup, miss = find(nums)
print(dup, miss)
