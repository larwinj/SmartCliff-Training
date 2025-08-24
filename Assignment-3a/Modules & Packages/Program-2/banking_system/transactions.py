def deposit(account, amount):
    account.balance += amount
    return account.balance

def withdraw(account, amount):
    if amount <= account.balance:
        account.balance -= amount
    else:
        print("Insufficient funds!")
    return account.balance