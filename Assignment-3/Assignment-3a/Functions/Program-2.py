def calculate_balance(initial_balance, transactions):
    return initial_balance + sum(transactions)


initial_balance = int(input("Enter the initial balance: "))
transactions = list(map(int, input("Enter the transactions: ").split()))
print(calculate_balance(initial_balance, transactions))