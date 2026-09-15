class BankAccount:
    bank_name = "ABC Bank"
    total_accounts = 0

    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance. Withdrawal cannot be completed.")
            return

        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")
        return self.balance

    def display_account_details(self):
        print("\n--- Account Details ---")
        print(f"Bank Name       : {BankAccount.bank_name}")
        print(f"Account Holder  : {self.account_holder_name}")
        print(f"Account Number  : {self.account_number}")
        print(f"Balance         : ₹{self.balance}")

    @classmethod
    def change_bank_name(cls, new_bank_name):
        cls.bank_name = new_bank_name