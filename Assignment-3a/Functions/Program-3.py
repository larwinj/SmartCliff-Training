def smallest_equal(nums):
    for i, val in enumerate(nums):
        if i % 10 == val:
            return i
    return -1

nums1 = list(map(int, input("Enter the elements: ").split()))
print(smallest_equal(nums1))

