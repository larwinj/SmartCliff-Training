from banking_system import account

from banking_system.account import Account
from banking_system.transactions import deposit,withdraw
from banking_system.loan import calculate_emi

name = input("Enter your name: ")
initial_balance = int(input("Enter your initial balance: "))
acc1 = Account(name, initial_balance)

deposit_amt = int(input("Enter your deposit amount: "))
deposit(acc1, deposit_amt)

withdraw_amt = int(input("Enter your withdraw amount: "))
withdraw(acc1, withdraw_amt)

print("Final Balance:", acc1.check_balance())
principal_amt = int(input("Enter your principal amount: "))
annual_rate = int(input("Enter your annual amount: "))
yr = int(input("Enter your year: "))
emi = calculate_emi(principal_amt, annual_rate, yr)
print("EMI:", emi)