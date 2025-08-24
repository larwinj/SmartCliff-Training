n1 = int(input())
nums1 = list(map(int, input().split()))

n2 = int(input())
nums2 = list(map(int, input().split()))

result = list(set(nums1) & set(nums2))
print(result)
