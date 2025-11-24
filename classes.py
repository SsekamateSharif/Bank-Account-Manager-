class BankAccount:
    def __init__(self, acc_number, owner, balance):
        self.acc_number = acc_number
        self.owner = owner 
        self.balance = balance 

    # function for depositing into the account 
    def deposit(self, amount):
        if amount > 0: # the amount deposited has to be greater than zero 
            self.balance = self.balance + amount 
            return f"Deposited {amount} New Balance {self.balance}"
        else:
            return "Invalid deposit amount"
    # withdraw function 
    def withdraw(self,amount):
        if amount <= 0:
            return f"Withdraw of {amount} is invalid"
        elif amount > self.balance:
            return f"Insufficient funds"
        else:
            self.balance = self.balance - amount 
            return f"Withdraw of {amount} successful. New balance: {self.balance}"
    # transfer function. 
    def transfer(self, amount, transfer_account_balance, target_account, target_owner):
        if amount <= 0:
            return f"Transfer amount invalid"
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            transfer_account_balance = transfer_account_balance + amount 
            self.balance -= amount 
            return f"Transfered {amount} to account {target_account} owned by {target_owner} New Balance for target: {transfer_account_balance}. Your New Balance: {self.balance}"
    # displaying the account details 
    def display(self):
        return f"Account number: {self.acc_number}| Owner: {self.owner} | Balance: {self.balance}"

     
        
        

        