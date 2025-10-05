# bank_account.py

class BankAccount:
    """A simple BankAccount class demonstrating OOP fundamentals."""

    def __init__(self, initial_balance=0.0):
        """Initialize account with an optional starting balance."""
        self.__account_balance = float(initial_balance)  # Encapsulated attribute

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False  # Not enough balance

    def display_balance(self):
        """Display the current balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """(Optional) Return the balance without printing."""
        return self.__account_balance
