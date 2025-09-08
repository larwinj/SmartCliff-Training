class PayOutOfBoundsException(Exception):
    def __init__(self, message="Transaction amount exceeds limit or insufficient balance."):
        super().__init__(message)


# Account Management Class
class AccountManagement:
    def __init__(self):
        self.current_balance = 80000
        self.max_transaction_limit = 30000

    def withdraw(self, amount):
        try:
            if amount > self.max_transaction_limit or amount > self.current_balance:
                raise PayOutOfBoundsException()
            else:
                self.current_balance -= amount
                print(f"Withdrawal successful. Updated balance: {self.current_balance}")
        except PayOutOfBoundsException as e:
            print(f"Error: {e}")


# ---------- Sample Test Cases ----------
if __name__ == "__main__":
    account = AccountManagement()

    amt = int(input("Enter the amount you want to withdraw: "))
    account.withdraw(amt)
