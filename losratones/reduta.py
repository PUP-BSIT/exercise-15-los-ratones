import random

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

    def create_account(self):
        owner_name = input("Enter your name: ")
        new_account = BankingSystem(owner=owner_name)
        bank_accounts[new_account.account_number] = new_account
                
        print(f"Account created! Number: {new_account.account_number}")
    
        self.owner = new_account.owner
        self.account_number = new_account.account_number
        self.balance = new_account.balance
        
        input(PAUSE_MESSAGE)
    
    def user_login(self):
        account_number = input("Enter your account number: ")
                
        if account_number in bank_accounts:
            account = bank_accounts[account_number]
            self.owner = account.owner
            self.account_number = account.account_number
            self.balance = account.balance
            print(f"Welcome! {self.owner}")    
        else:
            print("Account not found.")
            return False
        
        return True
        
    def deposit_cash(self):
        if not self.user_login():
            return 
        
        deposit_amount = input("Enter amount to deposit: ")
        
        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        
        if deposit_amount > 0:
            self.balance += deposit_amount
            bank_accounts[self.account_number].balance = self.balance
            print(
                f"Deposited {deposit_amount}, "
                f"New balance: {self.balance}"
                )
        else:
            print("Deposit amount must be positive.")
        
        input(PAUSE_MESSAGE)

    def withdraw_cash(self):
        if not self.user_login():
            return 
        
        withdraw_amount = input("Enter amount to withdraw: ")
        
        try:
            withdraw_amount = float(withdraw_amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        
        if 0 < withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            bank_accounts[self.account_number].balance = self.balance 
            print(f"Withdrew {withdraw_amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
            
        input(PAUSE_MESSAGE)

    def check_balance(self):
        if not self.user_login():
            return 
        
        print(f"Account balance: {self.balance}")
        input(PAUSE_MESSAGE)
        
    def transfer_cash(self):
        if not self.user_login():
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
        
        if 0 < transfer_amount <= self.balance:
            self.balance -= transfer_amount
            bank_accounts[self.account_number].balance = self.balance
            
            target_account = bank_accounts[target_account_number]
            target_account.balance += transfer_amount
            bank_accounts[target_account_number].balance = target_account.balance
            
            print(
                f"Transferred {transfer_amount} to "
                f"{target_account.owner}."
            )
        else:
            print("Transfer failed. Check amount and balance.")
            
        input(PAUSE_MESSAGE)

    def account_summary(self):
        if not self.user_login():
            return 
        
        print(
            f"Account {self.account_number} "
            f"owned by {self.owner} "
            f"with balance {self.balance}"
        )
        
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
        elif user_choice == "7":
            print("Thank you for using Banko Reduta!")
            return False
        else:
            print("Invalid choice. Please choose between 1 to 7.")
            return True
