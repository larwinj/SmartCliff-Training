# 8st code :

num = int(input("Enter a number: "))

count = 0
for d in str(num):
    digit = int(d)
    if num % digit == 0:
        count += 1

print(count)
