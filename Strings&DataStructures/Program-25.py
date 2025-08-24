def remove_duplicates(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


def calculate_sum(lst):
    return sum(lst)


def calculate_mean(lst):
    if len(lst) == 0:
        return 0
    return round(sum(lst) / len(lst), 2)


def find_min_max(lst):
    return min(lst), max(lst)


n = int(input("Enter number of integers (N): "))

# Step 2: Read integers
numbers = []
print("Enter the integers:")
for _ in range(n):
    numbers.append(int(input()))

# Step 3: Remove duplicates initially
unique_numbers = remove_duplicates(numbers)

# Step 4: Menu-driven loop
while True:
    print("\nMENU")
    print("1. Remove duplicates from the list")
    print("2. Calculate the sum of unique values in the list")
    print("3. Calculate the mean of unique values in the list")
    print("4. Find the largest and smallest unique values in the list")
    print("5. Quit the program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("List with duplicates removed:", unique_numbers)

    elif choice == 2:
        print("Sum of unique values:", calculate_sum(unique_numbers))

    elif choice == 3:
        print("Mean of unique values:", calculate_mean(unique_numbers))

    elif choice == 4:
        smallest, largest = find_min_max(unique_numbers)
        print("Smallest value:", smallest)
        print("Largest value:", largest)

    elif choice == 5:
        print("Quitting program.")
        break
    else:
        print("Invalid choice! Please try again.")