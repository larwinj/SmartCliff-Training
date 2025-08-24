class Account:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def check_balance(self):
        return self.balance
