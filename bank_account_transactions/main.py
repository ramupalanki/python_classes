from bank_account import BankAccount


account1 = BankAccount("Ravi", "1001", 5000)
account2 = BankAccount("Priya", "1002", 10000)

account1.display_account_details()
account2.display_account_details()

account1.deposit(2000)
account1.check_balance()

account1.withdraw(1500)
account1.check_balance()

# Trying to withdraw more than the available balance
account1.withdraw(10000)

# Change bank name for all accounts
BankAccount.change_bank_name("XYZ Bank")

account1.display_account_details()
account2.display_account_details()

print(f"\nTotal bank accounts created: {BankAccount.total_accounts}")