# 14th code :

num = input("Enter a 4-digit car number: ")

if not num.isdigit() or len(num) != 4:
    print("It is not a valid car number")
else:
    digit_sum = sum(int(d) for d in num)
    if digit_sum % 3 == 0 or digit_sum % 5 == 0 or digit_sum % 7 == 0:
        print("Can be my car number")
    else:
        print("Cannot be my car number")