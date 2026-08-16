class BankAccount:
    def __init__(self, name: str, starting_balance: float = 0.00):
        self.name = name
        self.balance = float(starting_balance)

    def deposit(self, amount: float):
        if amount <= 0:
            print(f"Deposit failed for {self.name}:Amount must be greater than zero.")
            return False
        self.balance += amount
        print(f"Deposited GHS {amount:.2f} to {self.name}'s account.")
        return True

    def withdraw(self, amount: float):
        if amount <= 0:
            print(f"Withdraw failed for {self.name}: Amount must be greater than zero.")
            return False
        if amount > self.balance:
            print(f"Withdraw failed for {self.name}: Insufficient funds!")
            return False
        self.balance -= amount
        print(f"Withdrew GHS {amount:.2f} from {self.name}'s account.")
        return True

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Account[{self.name}] | Balance: GHS {self.balance:2f}"

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Task 1 Demonstration ---")

    #1. Create two BankAccount instances with different names and starting balances
    acc1 = BankAccount("Ransford Ali", 600.00)
    acc2 = BankAccount ("Naa Amofa", 400.00)

    #2. Make at least three transactions across the two accounts
    acc1.deposit(300.00)
    acc2.deposit(200.00)
    acc1.withdraw(200.00)

    #3. Print each account after the transactions
    print(acc1)
    print(acc2)

    #4. Attempt a withdrwal that should fail and show it handles without crashing
    print("\nAttempting invalid withdrwal...")
    acc2.withdraw(3000.00)
    print(acc2)
    
    