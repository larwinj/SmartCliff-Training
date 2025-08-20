# 6st code :

# Function to check the leap year or not
def check(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def find(century_number):
    start_year = (century_number) * 100 + 1
    end_year = century_number * 100 + 100 - 1
    # print(start_year)
    print(f"Leap years in the {century_number}th century: ",end="")
    found_leap_years = 0
    # al = []
    for year in range(start_year, end_year + 1):
        if check(year):
            # al.append(year)
            found_leap_years+=1

    if found_leap_years != 0:
        # print(al)
        print(found_leap_years)
    else:
        print("No leap years found in this century.")


find(int(input("Enter century (e.g., 19 for 1901-2000): ")))