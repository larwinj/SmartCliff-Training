# 19th code :   Climbing Stairs

n = int(input())

if n <= 2:
  print(n)

else:
  # Also proved by the base of fibonacci series
  c,a,b = 0,1,2
  for i in range(3,n+1):
    c = a + b
    a=b
    b=c
  print(c)

