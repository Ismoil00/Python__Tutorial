class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
    
    def get_balance(self):
        print(f"\nAccount '{self.name} balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of {self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. 🚀")
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\nTransfer complete! ✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted: ❌ {error}")
            


#######################################################

Ismoil = BankAccount(5000, "ISMOIL")
Ismoil.get_balance()
Ismoil.deposit(520)
Ismoil.withdraw(6000)
Sorbon = BankAccount(9000, "SORBON")
Sorbon.get_balance()
Sorbon.deposit(1255)
Sorbon.withdraw(10255)