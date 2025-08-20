# 15th code :

num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid input")
else:
    fact = 1
    i = 1
    while fact < num:
        i += 1
        fact *= i
    if fact == num:
        print(i)
    else:
        print("Sorry. The given number is not a perfect factorial")