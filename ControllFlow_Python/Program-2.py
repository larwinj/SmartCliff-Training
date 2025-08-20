# 2st code :

import math

num = int(input())

# this is the formulae to find the length of the integer with O(1)
len = math.floor(math.log10(abs(num))) + 1

if len != 5:
  print("Not a valid number")
else:
  reversed_num = 0
  while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
  print(reversed_num)