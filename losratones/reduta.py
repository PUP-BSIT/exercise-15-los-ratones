import random

EXIT_OPTION = "7"
MIN_RANGE = 100000
MAX_RANGE = 999999
PAUSE_MESSAGE = "Press Enter to Continue..."
bank_accounts = {}

class BankingSystem:
    def __init__(self, owner="Guest", balance=0.0, account_number=None):
        if account_number is None:
            self.account_number = str(random.randint(MIN_RANGE, MAX_RANGE))
        else:
            self.account_number = account_number

        self.owner = owner
        self.balance = balance
        self.logged_in = False
        self.active_account = None

    def create_account(self):
        owner_name = input("Enter your name: ")
        new_account = BankingSystem(owner=owner_name)
        bank_accounts[new_account.account_number] = new_account

        print(f"Account created! Number: {new_account.account_number}")

        self.owner = new_account.owner
        self.account_number = new_account.account_number
        self.balance = new_account.balance

        input(PAUSE_MESSAGE)

    def deposit_cash(self):
        account = self.get_authenticated_account()
        if not account:
            return

        deposit_amount = input("Enter amount to deposit: ")

        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        if deposit_amount > 0:
            account.balance += deposit_amount
            bank_accounts[account.account_number].balance = account.balance
            print(
                f"Deposited {deposit_amount}, "
                f"New balance: {account.balance}"
            )
        else:
            print("Deposit amount must be positive.")

        input(PAUSE_MESSAGE)

    def withdraw_cash(self):
        account = self.get_authenticated_account()
        if not account:
            return

        withdraw_amount = input("Enter amount to withdraw: ")

        try:
            withdraw_amount = float(withdraw_amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return

        if 0 < withdraw_amount <= account.balance:
            account.balance -= withdraw_amount
            bank_accounts[account.account_number].balance = account.balance
            print(
                f"Withdrew {withdraw_amount}."
                f"New balance: {account.balance}"
                )
        else:
            print("Insufficient funds or invalid amount.")

        input(PAUSE_MESSAGE)

    def check_balance(self):
        account = self.get_authenticated_account()
        if not account:
            return

        print(f"Account balance: {account.balance}")
        input(PAUSE_MESSAGE)

    def transfer_cash(self):
        source_account = self.get_authenticated_account()
        if not source_account:
            return
        
        target_account_number = input("Enter target account number: ")
        
        if target_account_number not in bank_accounts:
            print("Target account not found.")
            return
        
        transfer_amount = input("Enter amount to transfer: ")
        
        try:
            transfer_amount = float(transfer_amount)
        except ValueError: 
            print("Invalid amount. Please enter a valid amount.")
            return
        
        if 0 < transfer_amount <= source_account.balance:
            source_account.balance -= transfer_amount
    
            target = bank_accounts[target_account_number]
            target.balance += transfer_amount
    
            summary = (
                f"Transferred {transfer_amount} "
                f"to {target.owner}."
            )
            print(summary)
        else:
            print("Transfer failed. Check amount and balance.")

        input(PAUSE_MESSAGE)

    def account_summary(self):
        account = self.get_authenticated_account()
        if not account:
            return

        summary = (
            f"Account {account.account_number} "
            f"owned by {account.owner} "
            f"with balance {account.balance}"
        )
        print(summary)
        
        input(PAUSE_MESSAGE)

    def menu(self):
        while True:
            self.display_menu()
            user_choice = input("Select an option(1 - 7): ")
            if not self.evaluate_choice(user_choice):
                break

    def display_menu(self):
        print("Welcome To Banko Reduta!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Account Summary")
        print("7. Exit")

    def evaluate_choice(self, user_choice):
        options = {
            "1": self.create_account,
            "2": self.deposit_cash,
            "3": self.withdraw_cash,
            "4": self.check_balance,
            "5": self.transfer_cash,
            "6": self.account_summary,
        }

        if user_choice in options:
            options[user_choice]()
            return True
        elif user_choice == EXIT_OPTION:
            self.logout() 
            print("Thank you for using Banko Reduta!")
            return False
        else:
            print("Invalid choice. Please choose between 1 to 7.")
            return True

    def get_authenticated_account(self):
        if self.logged_in and self.active_account:
            return self.active_account

        account_number = input("Enter your account number: ")

        if account_number in bank_accounts:
            account = bank_accounts[account_number] 
            print(f"Welcome! {account.owner}")
            
            self.logged_in = True
            self.active_account = account
            return account
        
        print("Account not found.")
        return None

    def logout(self):
        self.logged_in = False 
        self.active_account = None