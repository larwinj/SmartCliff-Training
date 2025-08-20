# 21th code :

num = int(input())


binary_str = bin(num)[2:]  #After retriving slicing the output

result = 0
count = 0

for i in binary_str:
    if i == '1':
        count += 1
        result = max(result, count)
    else:
        count = 0

print(result)
