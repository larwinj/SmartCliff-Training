# 11th code :

month = int(input())
year = int(input())
days = 0

# Stroing all months in the form of array to retrive easily
ar = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

if month < 1 or month > 12:
    print("Invalid month number")
else:
    if month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days = 29
        else:
            days = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    else:
        days = 30

    print(f"{ar[month-1]} {year} has {days} days")
