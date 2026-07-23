class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Success! {amount} PKR jama ho gaye. New Balance: {self.balance} PKR")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Success! {amount} PKR nikal liye gaye. New Balance: {self.balance} PKR")
        else:
            print("Insufficient balance or invalid amount!")

    def show_balance(self):
        print(f"Account Holder: {self.account_holder} | Current Balance: {self.balance} PKR")

# --- Testing the code ---
def main():
    print("Welcome to My Bank System")
    name = input("Enter your name: ")
    user_account = BankAccount(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amt = float(input("Amount to deposit: "))
            user_account.deposit(amt)
        elif choice == '2':
            amt = float(input("Amount to withdraw: "))
            user_account.withdraw(amt)
        elif choice == '3':
            user_account.show_balance()
        elif choice == '4':
            print("Thank you for using our service!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()