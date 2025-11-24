from classes import BankAccount 
Account_1 = BankAccount(1, "Sharif", 200)
Account_2 = BankAccount(2, "Rebbeca", 350)
Account_3 = BankAccount(3, "Sedrick", 450)
Account_4 = BankAccount(4, "Drake", 600)
Account_5 = BankAccount(5, "Sihab", 380)
# depositing to the bank accounts 
print(BankAccount.deposit(Account_1, 300))
print(BankAccount.deposit(Account_2, 200))
print(BankAccount.deposit(Account_3, 100))
print(BankAccount.deposit(Account_4, 250))
print(BankAccount.deposit(Account_5, 400))
# Withdrawing money 
print(BankAccount.withdraw(Account_1, 150))
print(BankAccount.withdraw(Account_3, 250))
print(BankAccount.withdraw(Account_4, 300))
# transfering money from one account to another 
print(BankAccount.transfer(Account_1, 300, 200, 3, "Fred"))
print(BankAccount.transfer(Account_5, 300, 150, 2, "Jackie"))

# displaying the account information 
print(BankAccount.display(Account_1))
print(BankAccount.display(Account_3))
print(BankAccount.display(Account_5))