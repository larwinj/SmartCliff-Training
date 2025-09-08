def longest_consecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                streak += 1

            longest = max(longest, streak)

    return longest

nums = list(map(int, input("Enter the elements: ").split()))
print(longest_consecutive(nums))