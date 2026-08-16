from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, name: str, starting_balance: float= 0.0, interest_rate: float = 0.0):
        super().__init__(name, starting_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        #Calculate interest based on current balance and rate percent
        interest_amount = self.balance * (self.interest_rate / 100)
        self.deposit(interest_amount)
        print(f"Apllied {self.interest_rate}% interest: GHS {interest_amount:.2f} added.")

    def __str__(self) -> str:
        return f"SavingsAccount[{self.name}] | Balance: GHS {self.balance:.2f} | Rate: {self.interest_rate}%"

# --- Demonstration ---
if __name__ == "__main__":
    print("\n--- Task 2 Demonstration ---")

    #1. Create a SavingsAccount
    savings_acc = SavingsAccount("Ransford Ali", 1000.00, 5.0)
    print(savings_acc)

    #2. Make two deposits
    savings_acc.deposit(300.00)
    savings_acc.deposit(250.00)

    #3. Call apply_interest and print the account to show the balance changed
    savings_acc.apply_interest()
    print(savings_acc)

    #4. Make a withdrawal and confirm it still works correctly
    savings_acc.withdraw(200.00)
    print(savings_acc)
