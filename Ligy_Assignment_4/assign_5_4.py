class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Example usage
account = BankAccount(initial_balance=1000)

account.deposit(500)
account.withdraw(200)
account.withdraw(1000)  # Attempting to withdraw more than the balance
account.deposit(-50)   # Attempting to deposit a negative amount

# Display the final balance
print(f"Final balance: ${account.balance}")
