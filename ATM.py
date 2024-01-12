class ATM:
    def __init__(self, name, balance=1000, transaction_history=[]):
        self.name = name
        self.balance = balance
        self.transaction_history = transaction_history

    def display_menu(self):
        print("\n===== ATM Interface =====")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Transactions History")
        print("5. Quit")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
            print(f"Withdrawal successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid amount or insufficient funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            print(f"Deposit successful. Updated balance: ${self.balance}")
        else:
            print("Invalid amount.")

    def transfer(self, amount, recipient):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transfer: ${amount} to {recipient.name}")
            print(f"Transfer successful. Remaining balance: ${self.balance}")
        else:
            print("Invalid amount or insufficient funds.")

    def display_transaction_history(self):
        print("\n===== Transaction History =====")
        for transaction in self.transaction_history:
            print(transaction)

if __name__ == "__main__":
    user_atm = ATM("User ATM")

    while True:
        user_atm.display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            amount = float(input("Enter the withdrawal amount: "))
            user_atm.withdraw(amount)
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            user_atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the transfer amount: "))
            recipient_name = input("Enter the recipient's name: ")
            recipient = ATM(recipient_name)
            user_atm.transfer(amount, recipient)
        elif choice == "4":
            user_atm.display_transaction_history()
        elif choice == "5":
            print("Exiting ATM. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")