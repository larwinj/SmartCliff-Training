def shuffle_list(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])      # take from first half
        result.append(nums[i + n])  # take from second half
    return result

n = int(input("Enter the number of elements: "))
nums = list(map(int, input("Enter the elements: ").split()))

print(shuffle_list(nums, n))
